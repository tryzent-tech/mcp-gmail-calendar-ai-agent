from langchain.agents import create_openai_functions_agent, AgentExecutor
from langchain import hub
from langchain_openai import ChatOpenAI
from composio_langchain import ComposioToolSet
import os
from dotenv import load_dotenv

load_dotenv()

composio_api_key = os.getenv("COMPOSIO_API_KEY")

llm = ChatOpenAI()
prompt = hub.pull("hwchase17/openai-functions-agent")

composio_toolset = ComposioToolSet(api_key= composio_api_key)
tools = composio_toolset.get_tools(actions=['GOOGLECALENDAR_CREATE_EVENT'])

agent = create_openai_functions_agent(llm, tools, prompt)
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

async def set_calender_event(message):
    flag = True
    task_execution_checker(message)
    if flag == False:
        return "No event found in the message"
    else:
        task = f"Use this data to create an event on google calender :- '{message}'."
        result = agent_executor.invoke({"input": task})
        print(result)
        return "Event Has been created succesfully on google calender"

def task_execution_checker(message):
    for i in message:
        if i == "None":
            flag = False
            break
        else:
            flag = True
    return flag