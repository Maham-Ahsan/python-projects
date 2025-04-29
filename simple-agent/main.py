import os
from dotenv import load_dotenv
from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel

#use this code for dont have cradit
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

agent = Agent(
    name="Greeting Agent",
    instructions="you are a Greeting Agent, Your task is to graet a user with afriendly message, when someone says hi you have to Response Salam from Maham, if someone says bye then you say Allah Hafiz from Maham, when someone  asks other then greeting then say Maham is here just for greeting,I can not answer anything else, sorry",
    model = model
)
           
           
user_question = input("please enter your Question: ")

result = Runner.run_sync(agent, user_question)
print(result.final_output) 