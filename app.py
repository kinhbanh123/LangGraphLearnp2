#set up
import os
from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_openai import OpenAI
from langchain_openai import ChatOpenAI
from langchain import hub
from langgraph.prebuilt import create_react_agent
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_google_genai import GoogleGenerativeAI


###########################################################################
load_dotenv() #Load something secret
huggingfacehub_api_token = os.getenv("HUGGINGFACEHUB_API_TOKEN")
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")
if not huggingfacehub_api_token:
    raise ValueError("HUGGINGFACEHUB_API_TOKEN is not set in the environment")
if not GOOGLE_API_KEY:
    raise ValueError("GOOGLE_API_KEY is not set in the enviroment")
if not OPENAI_API_KEY:
    raise ValueError("OPENAI_API_KEY is not set in the enviroment")
# Set up the Google model
#llm = ChatGoogleGenerativeAI(model="gemini-pro", google_api_key=GOOGLE_API_KEY)
#llm = OpenAI(openai_api_key=OPENAI_API_KEY,temperature=0.1, streaming=True)
# Set up the HuggingFace model
#llm = GoogleGenerativeAI(model="models/text-bison-001", google_api_key=GOOGLE_API_KEY)
#llm = ChatOpenAI(model="gpt-4-turbo-preview", openai_api_key=OPENAI_API_KEY)
"""repo_id = "HuggingFaceH4/zephyr-7b-beta"
llm = HuggingFaceHub(huggingfacehub_api_token=huggingfacehub_api_token,
                    repo_id=repo_id,
                   model_kwargs={"temperature":0.01, "max_new_tokens":1000},
                   streaming=True) #swap model if you wanna"""
tools = [TavilySearchResults(max_results=3)]
prompt = hub.pull("wfh/react-agent-executor")
prompt.pretty_print()
template = """
<|system|>>
U need to find what is the main idea of the question
</s>
<|user|>
{query}
</s>
<|assistant|>
"""
###########################################################################
agent_executor = create_react_agent(llm, tools, messages_modifier=prompt)
###########################################################################
