import sys
import types

# Create dummy langchain and related modules for tests
langchain = types.ModuleType('langchain')
langchain.hub = types.SimpleNamespace(pull=lambda *a, **k: None)
agents = types.ModuleType('langchain.agents')
class DummyExecutor:
    def __init__(self, *a, **kw):
        pass
    def invoke(self, *a, **kw):
        return {}
agents.create_openai_functions_agent = lambda *a, **k: None
agents.AgentExecutor = DummyExecutor
langchain.agents = agents
sys.modules.setdefault('langchain', langchain)
sys.modules.setdefault('langchain.agents', agents)

langchain_openai = types.ModuleType('langchain_openai')
langchain_openai.ChatOpenAI = object
sys.modules.setdefault('langchain_openai', langchain_openai)

composio_langchain = types.ModuleType('composio_langchain')
composio_langchain.ComposioToolSet = lambda *a, **kw: types.SimpleNamespace(get_tools=lambda actions: [])
sys.modules.setdefault('composio_langchain', composio_langchain)

dotenv = types.ModuleType('dotenv')
dotenv.load_dotenv = lambda *a, **kw: None
sys.modules.setdefault('dotenv', dotenv)
