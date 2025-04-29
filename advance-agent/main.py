import os
import chainlit as cl
from dotenv import load_dotenv
from typing import Optional, Dict
from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel
from agents.tool import function_tool 

load_dotenv()

gemini_api_key = os.getenv("GEMINI_API_KEY")

provider = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai",
)

model = OpenAIChatCompletionsModel(
    model = "gemini-2.0-flash",
    openai_client= provider
)
@function_tool("get_weather")
def get_weather(Location:str, unit:str= "C") -> str:
    """Fetch the weather for a given location,  return the weather """

    return f"The weather in {Location} is 22 degrees {unit}"

agent = Agent(
    name="Greeting Agent",
    instructions="you are a Greeting Agent, Your task is to graet a user with afriendly message, when someone says hi you have to Response Salam from Maham, If someone asks about the weather then use the get_weather tool to get the weather,if someone says bye then you say Allah Hafiz from Maham, when someone  asks other then greeting then say Maham is here just for greeting,I can not answer anything else, sorry",
    model = model,
    tools=[get_weather]
)

@cl.oauth_callback
def oauth_callback(
    provider_id: str,
    token: str,
    raw_user_data: Dict[str, str],
    default_user: cl.User,
) -> Optional[cl.User]:

    print(f"provider: {provider_id}")
    print(f"user data: {raw_user_data}")

    return default_user

@cl.on_chat_start
async def handle_chat_start():

    cl.user_session.set("history", [])

    await cl.Message(content="Hello! How can I help you?").send()

@cl.on_message
async def handle_message(message: cl.Message):

    history = cl.user_session.get("history")

    history.append({"role": "user", "content": message.content})

    result = await cl.make_async(Runner.run_sync)(agent, input=history)

    response_text = result.final_output
    await cl.Message(content=response_text).send()

    history.append({"role": "assistant", "content": response_text})
    cl.user_session.set("history",history)