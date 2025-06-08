from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel, function_tool
from agents.run import RunConfig
from dotenv import load_dotenv
from typing import cast , List
import chainlit as cl
import os

load_dotenv()
gemini_api_key = os.getenv('GEMINI_API_KEY')

if not gemini_api_key:
    raise ValueError("GEMINI_API_KEY environment variable is not set. Please set it to your Gemini API key.")

@function_tool
def get_inventory():
    inventory = {
        "Shampoo" : 4,
        "Soap" : 7,
        "Hair oil" : 5,
    }
    return inventory


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

    # Create a new agent with the specified model and instructions
    agent: Agent = Agent(
        name="Assistant",
        instructions="You are a helpful assistant",
        model=model
        )
    quantity_agent : Agent = Agent(
        name= 'quantity checker',
        instructions= "You are a quantity checker agent, you Check the quantity of the given product and tell the user how many pieces of that product are available. only use 'get_inventory' tool to get informaton. If user asks something that is not in the your data, reply with 'Product not available'.",
        model=model,
        tools=[get_inventory]

    )
    
    # Initialize chat history and configuration in user session
    cl.user_session.set("chat_history", [] )
    cl.user_session.set("config", config)   
    cl.user_session.set("agent", agent)
    cl.user_session.set("quantity_agent", quantity_agent)

    # Send a welcome message to the user
    await cl.Message(content="Welcome I am management AI Assistant! How can I help you today?").send()


@cl.on_message
async def main(message : cl.Message):
    """Process incoming messages and generate responses."""
    # create a new message 
    msg = cl.Message("")
    await msg.send()

    agent: Agent = cast(Agent, cl.user_session.get("agent"))
    config: RunConfig = cast( RunConfig, cl.user_session.get("config"))
    history = cl.user_session.get("chat_history") or []
    
    history.append({"role": "user", "content": message.content})
    try:
        print("\n[CALLING_AGENT_WITH_CONTEXT]\n", history, "\n")

        result = Runner.run_streamed(agent , history , run_config=config)

        async for event in result.stream_events():
            if event.type == "raw_response_event" and hasattr(event.data, 'delta'):
                token = event.data.delta
                await msg.stream_token(token)



        history.append({"role": "assistant", "content": msg.content})  
        # Update the session with the new history.
        cl.user_session.set("chat_history", history)
        
        # Optional: Log the interaction
        print(f"User: {message.content}")
        print(f"Assistant: {msg.content}")



    except Exception as e:
        msg.content = f"Error: {str(e)}"
        await msg.update()
        print(f"Error: {str(e)}")
        