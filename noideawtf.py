{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "c:\\Users\\tnguy\\AppData\\Local\\Programs\\Python\\Python312\\Lib\\site-packages\\tqdm\\auto.py:21: TqdmWarning: IProgress not found. Please update jupyter and ipywidgets. See https://ipywidgets.readthedocs.io/en/stable/user_install.html\n",
      "  from .autonotebook import tqdm as notebook_tqdm\n"
     ]
    }
   ],
   "source": [
    "from typing import List\n",
    "import os\n",
    "from langchain_core.messages import SystemMessage\n",
    "from langchain_core.pydantic_v1 import BaseModel\n",
    "from langchain_google_genai import ChatGoogleGenerativeAI\n",
    "from langchain_openai import ChatOpenAI\n",
    "from dotenv import load_dotenv\n",
    "from langchain_community.utilities import OpenWeatherMapAPIWrapper\n",
    "from langchain_community.tools.openweathermap import OpenWeatherMapQueryRun\n",
    "from langchain_core.utils.function_calling import convert_to_openai_function\n",
    "from langgraph.graph import Graph\n",
    "from typing import TypedDict, Annotated, Sequence\n",
    "import operator\n",
    "from langchain_core.messages import BaseMessage\n",
    "from langchain_core.tools import tool\n",
    "import requests"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "load_dotenv()\n",
    "GOOGLE_API_KEY = os.getenv(\"GOOGLE_API_KEY\")\n",
    "OPENAI_API_KEY = os.getenv(\"OPENAI_API_KEY\")\n",
    "TAVILY_API_KEY = os.getenv(\"TAVILY_API_KEY\")\n",
    "os.environ[\"OPENWEATHERMAP_API_KEY\"] = os.environ.get(\"OPENWEATHERMAP_API_KEY\")\n",
    "class AgentState(TypedDict):\n",
    "    messages: Annotated[Sequence[BaseMessage], operator.add]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.1"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
