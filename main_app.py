import os
from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAI
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_openai import OpenAI
from langchain_openai import ChatOpenAI
from langchain import hub
from langgraph.prebuilt import create_react_agent
from langchain_community.tools.tavily_search import TavilySearchResults
from langgraph.graph import Graph

######################################################################

######################################################################
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
llm = ChatGoogleGenerativeAI(model="gemini-pro", google_api_key=GOOGLE_API_KEY)

#llm = OpenAI(openai_api_key=OPENAI_API_KEY,temperature=0.1, streaming=True)
# Set up the HuggingFace model
#llm = GoogleGenerativeAI(model="models/text-bison-001", google_api_key=GOOGLE_API_KEY)
#llm = ChatOpenAI(model="gpt-4-turbo-preview", openai_api_key=OPENAI_API_KEY)
"""repo_id = "HuggingFaceH4/zephyr-7b-beta"
llm = HuggingFaceHub(huggingfacehub_api_token=huggingfacehub_api_token,
                    repo_id=repo_id,
                   model_kwargs={"temperature":0.01, "max_new_tokens":1000},
                   streaming=True) #swap model if you wanna"""
############################################################

#print(llm.invoke('Hey there').content)
def function_1(input_1):
    response = llm.invoke(input_1)
    return response.content

def function_2(input_2):
    return "Agent Says: " + input_2
# Define a Langchain graph
workflow = Graph()

#calling node 1 as agent
workflow.add_node("agent", function_1)
workflow.add_node("node_2", function_2)

workflow.add_edge('agent', 'node_2')

workflow.set_entry_point("agent")
workflow.set_finish_point("node_2")

app = workflow.compile()



