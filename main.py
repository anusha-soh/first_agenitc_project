from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel
from agents.run import RunConfig
from dotenv import load_dotenv
import os
import chainlit as cl

gemini_api_key = os.getenv('GEMINI_API_KEY')

load_dotenv()

#Reference: https://ai.google.dev/gemini-api/docs/openai
# # First we create Client?provider from here API connects to cloud and actract data or send or receive request
external_client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)
# # Now we create model here ve specify our model and frpm where to extract data (client)
model = OpenAIChatCompletionsModel(
    model = "gemini-2.0-flash",
    openai_client= external_client
)


gernal_info_agent = Agent(
    name = "Anush",
    instructions ="You are a professional assistant. You are helpful, creative, clever, and very friendly. You answer questions in a concise manner.",
    model = model

)


config = RunConfig(
    model=model,
    model_provider=external_client,
    tracing_disabled=True
)



@cl.on_message
async def main(message : cl.Message):
    user_input = message.content
    result = Runner.run_sync(gernal_info_agent , user_input , run_config=config)
    await cl.Message(
        content=f"{result.final_output}",
    ).send()
