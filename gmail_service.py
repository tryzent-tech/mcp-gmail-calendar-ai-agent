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

composio_toolset = ComposioToolSet(api_key=composio_api_key)
tools = composio_toolset.get_tools(actions=['GMAIL_FETCH_MESSAGE_BY_MESSAGE_ID'])

agent = create_openai_functions_agent(llm, tools, prompt)
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

async def get_mail_content(message_id):
    task = f" Fetch the message :- '{message_id}'. And determine if the message contains a deadline or a scheduled event or not. If it does the return the summary of the event with the date and time it has been scheduled on otherwise just return the keyword 'None' and nothing else"
    result = agent_executor.invoke({"input": task})
    print(result)
    print(result['output'])
    return result["output"]