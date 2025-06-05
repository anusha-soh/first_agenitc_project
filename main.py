from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel
from agents.run import RunConfig
from dotenv import load_dotenv
from typing import cast
import chainlit as cl
import os

load_dotenv()
gemini_api_key = os.getenv('GEMINI_API_KEY')

# Check if the API key is present; if not, raise an error
if not gemini_api_key:
    raise ValueError("GEMINI_API_KEY is not set. Please ensure it is defined in your .env file.")



@cl.on_chat_start
async def start():

    external_client = AsyncOpenAI(
        api_key=gemini_api_key,
        base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
    )
    # # Now we create model here ve specify our model and frpm where to extract data (client)
    model = OpenAIChatCompletionsModel(
        model = "gemini-2.0-flash",
        openai_client= external_client
    )


    config = RunConfig(
        model=model,
        model_provider=external_client,
        tracing_disabled=True
    )

    """set up the chat session when user connect"""
    cl.user_session.set("chat_history", [] )

    cl.user_session.set("config", config)

    agent: Agent = Agent(
        name="Assistant",
        instructions="You are a helpful assistant",
        model=model
        )
    
    cl.user_session.set("agent", agent)

    await cl.Message(content="Welcome I am inventory management AI Assistant! How can I help you today?").send()


    # gernal_info_agent = Agent(
    #     name = "Anush",
    #     instructions ="You are a professional assistant. You are helpful, creative, clever, and very friendly. You answer questions in a concise manner.",
    #     model = model
# )

@cl.on_message
async def main(message : cl.Message):
    """Process incoming messages and generate responses."""
    # thinking message
    msg = cl.Message("Thinking...")
    await msg.send()

    agent: Agent = cast(Agent, cl.user_session.get("agent"))
    config: RunConfig = cast(RunConfig, cl.user_session.get("config"))

    history = cl.user_session.get("chat_history") or []
    history.append({"role": "user", "content": message.content})
    
    try:
        print("\n[CALLING_AGENT_WITH_CONTEXT]\n", history, "\n")

        result = Runner.run_sync(agent , history , run_config=config)

        response_content = result.final_output

        msg.content = response_content
        await msg.update()

        # Update the session with the new history.
        cl.user_session.set("chat_history", result.to_input_list())
        
        # Optional: Log the interaction
        print(f"User: {message.content}")
        print(f"Assistant: {response_content}")



    except Exception as e:
        msg.content = f"Error: {str(e)}"
        await msg.update()
        print(f"Error: {str(e)}")
        