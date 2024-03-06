{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Coding Assistant"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Requirement already satisfied: langchain in /opt/conda/lib/python3.11/site-packages (from -r requirements.txt (line 1)) (0.0.347)\n",
      "Requirement already satisfied: langchain-experimental in /opt/conda/lib/python3.11/site-packages (from -r requirements.txt (line 2)) (0.0.44)\n",
      "Requirement already satisfied: langchainhub in /opt/conda/lib/python3.11/site-packages (from -r requirements.txt (line 3)) (0.1.14)\n",
      "Requirement already satisfied: langchain-cli in /opt/conda/lib/python3.11/site-packages (from -r requirements.txt (line 4)) (0.0.19)\n",
      "Requirement already satisfied: openai in /opt/conda/lib/python3.11/site-packages (from -r requirements.txt (line 6)) (1.3.7)\n",
      "Requirement already satisfied: python-dotenv in /opt/conda/lib/python3.11/site-packages (from -r requirements.txt (line 7)) (1.0.0)\n",
      "Requirement already satisfied: google-search-results in /opt/conda/lib/python3.11/site-packages (from -r requirements.txt (line 8)) (2.4.2)\n",
      "Requirement already satisfied: faiss-cpu in /opt/conda/lib/python3.11/site-packages (from -r requirements.txt (line 9)) (1.7.4)\n",
      "Requirement already satisfied: pypdf in /opt/conda/lib/python3.11/site-packages (from -r requirements.txt (line 10)) (3.17.1)\n",
      "Requirement already satisfied: tqdm in /opt/conda/lib/python3.11/site-packages (from -r requirements.txt (line 11)) (4.66.1)\n",
      "Requirement already satisfied: wikipedia in /opt/conda/lib/python3.11/site-packages (from -r requirements.txt (line 12)) (1.4.0)\n",
      "Requirement already satisfied: arxiv in /opt/conda/lib/python3.11/site-packages (from -r requirements.txt (line 13)) (2.0.0)\n",
      "Requirement already satisfied: atlassian-python-api in /opt/conda/lib/python3.11/site-packages (from -r requirements.txt (line 14)) (3.41.4)\n",
      "Requirement already satisfied: numexpr in /opt/conda/lib/python3.11/site-packages (from -r requirements.txt (line 15)) (2.8.7)\n",
      "Requirement already satisfied: beautifulsoup4 in /opt/conda/lib/python3.11/site-packages (from -r requirements.txt (line 16)) (4.12.2)\n",
      "Requirement already satisfied: lxml in /opt/conda/lib/python3.11/site-packages (from -r requirements.txt (line 17)) (4.9.3)\n",
      "Requirement already satisfied: tiktoken in /opt/conda/lib/python3.11/site-packages (from -r requirements.txt (line 18)) (0.5.2)\n",
      "Requirement already satisfied: ipydatagrid in /opt/conda/lib/python3.11/site-packages (from -r requirements.txt (line 19)) (1.2.0)\n",
      "Requirement already satisfied: bqplot in /opt/conda/lib/python3.11/site-packages (from -r requirements.txt (line 20)) (0.12.42)\n",
      "Requirement already satisfied: langserve[all] in /opt/conda/lib/python3.11/site-packages (from -r requirements.txt (line 5)) (0.0.34)\n",
      "Requirement already satisfied: PyYAML>=5.3 in /opt/conda/lib/python3.11/site-packages (from langchain->-r requirements.txt (line 1)) (6.0.1)\n",
      "Requirement already satisfied: SQLAlchemy<3,>=1.4 in /opt/conda/lib/python3.11/site-packages (from langchain->-r requirements.txt (line 1)) (2.0.22)\n",
      "Requirement already satisfied: aiohttp<4.0.0,>=3.8.3 in /opt/conda/lib/python3.11/site-packages (from langchain->-r requirements.txt (line 1)) (3.9.1)\n",
      "Requirement already satisfied: anyio<4.0 in /opt/conda/lib/python3.11/site-packages (from langchain->-r requirements.txt (line 1)) (3.7.1)\n",
      "Requirement already satisfied: dataclasses-json<0.7,>=0.5.7 in /opt/conda/lib/python3.11/site-packages (from langchain->-r requirements.txt (line 1)) (0.6.3)\n",
      "Requirement already satisfied: jsonpatch<2.0,>=1.33 in /opt/conda/lib/python3.11/site-packages (from langchain->-r requirements.txt (line 1)) (1.33)\n",
      "Requirement already satisfied: langchain-core<0.1,>=0.0.11 in /opt/conda/lib/python3.11/site-packages (from langchain->-r requirements.txt (line 1)) (0.0.11)\n",
      "Requirement already satisfied: langsmith<0.1.0,>=0.0.63 in /opt/conda/lib/python3.11/site-packages (from langchain->-r requirements.txt (line 1)) (0.0.69)\n",
      "Requirement already satisfied: numpy<2,>=1 in /opt/conda/lib/python3.11/site-packages (from langchain->-r requirements.txt (line 1)) (1.26.2)\n",
      "Requirement already satisfied: pydantic<3,>=1 in /opt/conda/lib/python3.11/site-packages (from langchain->-r requirements.txt (line 1)) (2.5.2)\n",
      "Requirement already satisfied: requests<3,>=2 in /opt/conda/lib/python3.11/site-packages (from langchain->-r requirements.txt (line 1)) (2.31.0)\n",
      "Requirement already satisfied: tenacity<9.0.0,>=8.1.0 in /opt/conda/lib/python3.11/site-packages (from langchain->-r requirements.txt (line 1)) (8.2.3)\n",
      "Requirement already satisfied: types-requests<3.0.0.0,>=2.31.0.2 in /opt/conda/lib/python3.11/site-packages (from langchainhub->-r requirements.txt (line 3)) (2.31.0.10)\n",
      "Requirement already satisfied: gitpython<4.0.0,>=3.1.40 in /opt/conda/lib/python3.11/site-packages (from langchain-cli->-r requirements.txt (line 4)) (3.1.40)\n",
      "Requirement already satisfied: tomlkit<0.13.0,>=0.12.2 in /opt/conda/lib/python3.11/site-packages (from langchain-cli->-r requirements.txt (line 4)) (0.12.3)\n",
      "Requirement already satisfied: typer<0.10.0,>=0.9.0 in /opt/conda/lib/python3.11/site-packages (from typer[all]<0.10.0,>=0.9.0->langchain-cli->-r requirements.txt (line 4)) (0.9.0)\n",
      "Requirement already satisfied: uvicorn<0.24.0,>=0.23.2 in /opt/conda/lib/python3.11/site-packages (from langchain-cli->-r requirements.txt (line 4)) (0.23.2)\n",
      "Requirement already satisfied: fastapi<1,>=0.90.1 in /opt/conda/lib/python3.11/site-packages (from langserve[all]->-r requirements.txt (line 5)) (0.104.1)\n",
      "Requirement already satisfied: httpx>=0.23.0 in /opt/conda/lib/python3.11/site-packages (from langserve[all]->-r requirements.txt (line 5)) (0.25.2)\n",
      "Requirement already satisfied: httpx-sse>=0.3.1 in /opt/conda/lib/python3.11/site-packages (from langserve[all]->-r requirements.txt (line 5)) (0.3.1)\n",
      "Requirement already satisfied: orjson>=2 in /opt/conda/lib/python3.11/site-packages (from langserve[all]->-r requirements.txt (line 5)) (3.9.10)\n",
      "Requirement already satisfied: sse-starlette<2.0.0,>=1.3.0 in /opt/conda/lib/python3.11/site-packages (from langserve[all]->-r requirements.txt (line 5)) (1.8.2)\n",
      "Requirement already satisfied: distro<2,>=1.7.0 in /opt/conda/lib/python3.11/site-packages (from openai->-r requirements.txt (line 6)) (1.8.0)\n",
      "Requirement already satisfied: sniffio in /opt/conda/lib/python3.11/site-packages (from openai->-r requirements.txt (line 6)) (1.3.0)\n",
      "Requirement already satisfied: typing-extensions<5,>=4.5 in /opt/conda/lib/python3.11/site-packages (from openai->-r requirements.txt (line 6)) (4.8.0)\n",
      "Requirement already satisfied: feedparser==6.0.10 in /opt/conda/lib/python3.11/site-packages (from arxiv->-r requirements.txt (line 13)) (6.0.10)\n",
      "Requirement already satisfied: sgmllib3k in /opt/conda/lib/python3.11/site-packages (from feedparser==6.0.10->arxiv->-r requirements.txt (line 13)) (1.0.0)\n",
      "Requirement already satisfied: charset-normalizer<4,>=2 in /opt/conda/lib/python3.11/site-packages (from requests<3,>=2->langchain->-r requirements.txt (line 1)) (3.3.0)\n",
      "Requirement already satisfied: idna<4,>=2.5 in /opt/conda/lib/python3.11/site-packages (from requests<3,>=2->langchain->-r requirements.txt (line 1)) (3.4)\n",
      "Requirement already satisfied: urllib3<3,>=1.21.1 in /opt/conda/lib/python3.11/site-packages (from requests<3,>=2->langchain->-r requirements.txt (line 1)) (2.0.7)\n",
      "Requirement already satisfied: certifi>=2017.4.17 in /opt/conda/lib/python3.11/site-packages (from requests<3,>=2->langchain->-r requirements.txt (line 1)) (2023.7.22)\n",
      "Requirement already satisfied: deprecated in /opt/conda/lib/python3.11/site-packages (from atlassian-python-api->-r requirements.txt (line 14)) (1.2.14)\n",
      "Requirement already satisfied: six in /opt/conda/lib/python3.11/site-packages (from atlassian-python-api->-r requirements.txt (line 14)) (1.16.0)\n",
      "Requirement already satisfied: oauthlib in /opt/conda/lib/python3.11/site-packages (from atlassian-python-api->-r requirements.txt (line 14)) (3.2.2)\n",
      "Requirement already satisfied: requests-oauthlib in /opt/conda/lib/python3.11/site-packages (from atlassian-python-api->-r requirements.txt (line 14)) (1.3.1)\n",
      "Requirement already satisfied: soupsieve>1.2 in /opt/conda/lib/python3.11/site-packages (from beautifulsoup4->-r requirements.txt (line 16)) (2.5)\n",
      "Requirement already satisfied: regex>=2022.1.18 in /opt/conda/lib/python3.11/site-packages (from tiktoken->-r requirements.txt (line 18)) (2023.10.3)\n",
      "Requirement already satisfied: ipywidgets<9,>=7.6 in /opt/conda/lib/python3.11/site-packages (from ipydatagrid->-r requirements.txt (line 19)) (8.1.1)\n",
      "Requirement already satisfied: pandas>=1.3.5 in /opt/conda/lib/python3.11/site-packages (from ipydatagrid->-r requirements.txt (line 19)) (2.1.3)\n",
      "Requirement already satisfied: py2vega>=0.5 in /opt/conda/lib/python3.11/site-packages (from ipydatagrid->-r requirements.txt (line 19)) (0.6.1)\n",
      "Requirement already satisfied: traitlets>=4.3.0 in /opt/conda/lib/python3.11/site-packages (from bqplot->-r requirements.txt (line 20)) (5.11.2)\n",
      "Requirement already satisfied: traittypes>=0.0.6 in /opt/conda/lib/python3.11/site-packages (from bqplot->-r requirements.txt (line 20)) (0.2.1)\n",
      "Requirement already satisfied: attrs>=17.3.0 in /opt/conda/lib/python3.11/site-packages (from aiohttp<4.0.0,>=3.8.3->langchain->-r requirements.txt (line 1)) (23.1.0)\n",
      "Requirement already satisfied: multidict<7.0,>=4.5 in /opt/conda/lib/python3.11/site-packages (from aiohttp<4.0.0,>=3.8.3->langchain->-r requirements.txt (line 1)) (6.0.4)\n",
      "Requirement already satisfied: yarl<2.0,>=1.0 in /opt/conda/lib/python3.11/site-packages (from aiohttp<4.0.0,>=3.8.3->langchain->-r requirements.txt (line 1)) (1.9.4)\n",
      "Requirement already satisfied: frozenlist>=1.1.1 in /opt/conda/lib/python3.11/site-packages (from aiohttp<4.0.0,>=3.8.3->langchain->-r requirements.txt (line 1)) (1.4.0)\n",
      "Requirement already satisfied: aiosignal>=1.1.2 in /opt/conda/lib/python3.11/site-packages (from aiohttp<4.0.0,>=3.8.3->langchain->-r requirements.txt (line 1)) (1.3.1)\n",
      "Requirement already satisfied: marshmallow<4.0.0,>=3.18.0 in /opt/conda/lib/python3.11/site-packages (from dataclasses-json<0.7,>=0.5.7->langchain->-r requirements.txt (line 1)) (3.20.1)\n",
      "Requirement already satisfied: typing-inspect<1,>=0.4.0 in /opt/conda/lib/python3.11/site-packages (from dataclasses-json<0.7,>=0.5.7->langchain->-r requirements.txt (line 1)) (0.9.0)\n",
      "Requirement already satisfied: starlette<0.28.0,>=0.27.0 in /opt/conda/lib/python3.11/site-packages (from fastapi<1,>=0.90.1->langserve[all]->-r requirements.txt (line 5)) (0.27.0)\n",
      "Requirement already satisfied: gitdb<5,>=4.0.1 in /opt/conda/lib/python3.11/site-packages (from gitpython<4.0.0,>=3.1.40->langchain-cli->-r requirements.txt (line 4)) (4.0.11)\n",
      "Requirement already satisfied: httpcore==1.* in /opt/conda/lib/python3.11/site-packages (from httpx>=0.23.0->langserve[all]->-r requirements.txt (line 5)) (1.0.2)\n",
      "Requirement already satisfied: h11<0.15,>=0.13 in /opt/conda/lib/python3.11/site-packages (from httpcore==1.*->httpx>=0.23.0->langserve[all]->-r requirements.txt (line 5)) (0.14.0)\n",
      "Requirement already satisfied: comm>=0.1.3 in /opt/conda/lib/python3.11/site-packages (from ipywidgets<9,>=7.6->ipydatagrid->-r requirements.txt (line 19)) (0.1.4)\n",
      "Requirement already satisfied: ipython>=6.1.0 in /opt/conda/lib/python3.11/site-packages (from ipywidgets<9,>=7.6->ipydatagrid->-r requirements.txt (line 19)) (8.16.1)\n",
      "Requirement already satisfied: widgetsnbextension~=4.0.9 in /opt/conda/lib/python3.11/site-packages (from ipywidgets<9,>=7.6->ipydatagrid->-r requirements.txt (line 19)) (4.0.9)\n",
      "Requirement already satisfied: jupyterlab-widgets~=3.0.9 in /opt/conda/lib/python3.11/site-packages (from ipywidgets<9,>=7.6->ipydatagrid->-r requirements.txt (line 19)) (3.0.9)\n",
      "Requirement already satisfied: jsonpointer>=1.9 in /opt/conda/lib/python3.11/site-packages (from jsonpatch<2.0,>=1.33->langchain->-r requirements.txt (line 1)) (2.4)\n",
      "Requirement already satisfied: python-dateutil>=2.8.2 in /opt/conda/lib/python3.11/site-packages (from pandas>=1.3.5->ipydatagrid->-r requirements.txt (line 19)) (2.8.2)\n",
      "Requirement already satisfied: pytz>=2020.1 in /opt/conda/lib/python3.11/site-packages (from pandas>=1.3.5->ipydatagrid->-r requirements.txt (line 19)) (2023.3.post1)\n",
      "Requirement already satisfied: tzdata>=2022.1 in /opt/conda/lib/python3.11/site-packages (from pandas>=1.3.5->ipydatagrid->-r requirements.txt (line 19)) (2023.3)\n",
      "Requirement already satisfied: gast<0.5,>=0.4.0 in /opt/conda/lib/python3.11/site-packages (from py2vega>=0.5->ipydatagrid->-r requirements.txt (line 19)) (0.4.0)\n",
      "Requirement already satisfied: annotated-types>=0.4.0 in /opt/conda/lib/python3.11/site-packages (from pydantic<3,>=1->langchain->-r requirements.txt (line 1)) (0.6.0)\n",
      "Requirement already satisfied: pydantic-core==2.14.5 in /opt/conda/lib/python3.11/site-packages (from pydantic<3,>=1->langchain->-r requirements.txt (line 1)) (2.14.5)\n",
      "Requirement already satisfied: greenlet!=0.4.17 in /opt/conda/lib/python3.11/site-packages (from SQLAlchemy<3,>=1.4->langchain->-r requirements.txt (line 1)) (3.0.0)\n",
      "Requirement already satisfied: click<9.0.0,>=7.1.1 in /opt/conda/lib/python3.11/site-packages (from typer<0.10.0,>=0.9.0->typer[all]<0.10.0,>=0.9.0->langchain-cli->-r requirements.txt (line 4)) (8.1.7)\n",
      "Requirement already satisfied: colorama<0.5.0,>=0.4.3 in /opt/conda/lib/python3.11/site-packages (from typer[all]<0.10.0,>=0.9.0->langchain-cli->-r requirements.txt (line 4)) (0.4.6)\n",
      "Requirement already satisfied: shellingham<2.0.0,>=1.3.0 in /opt/conda/lib/python3.11/site-packages (from typer[all]<0.10.0,>=0.9.0->langchain-cli->-r requirements.txt (line 4)) (1.5.4)\n",
      "Requirement already satisfied: rich<14.0.0,>=10.11.0 in /opt/conda/lib/python3.11/site-packages (from typer[all]<0.10.0,>=0.9.0->langchain-cli->-r requirements.txt (line 4)) (13.7.0)\n",
      "Requirement already satisfied: wrapt<2,>=1.10 in /opt/conda/lib/python3.11/site-packages (from deprecated->atlassian-python-api->-r requirements.txt (line 14)) (1.16.0)\n",
      "Requirement already satisfied: smmap<6,>=3.0.1 in /opt/conda/lib/python3.11/site-packages (from gitdb<5,>=4.0.1->gitpython<4.0.0,>=3.1.40->langchain-cli->-r requirements.txt (line 4)) (5.0.1)\n",
      "Requirement already satisfied: backcall in /opt/conda/lib/python3.11/site-packages (from ipython>=6.1.0->ipywidgets<9,>=7.6->ipydatagrid->-r requirements.txt (line 19)) (0.2.0)\n",
      "Requirement already satisfied: decorator in /opt/conda/lib/python3.11/site-packages (from ipython>=6.1.0->ipywidgets<9,>=7.6->ipydatagrid->-r requirements.txt (line 19)) (5.1.1)\n",
      "Requirement already satisfied: jedi>=0.16 in /opt/conda/lib/python3.11/site-packages (from ipython>=6.1.0->ipywidgets<9,>=7.6->ipydatagrid->-r requirements.txt (line 19)) (0.19.1)\n",
      "Requirement already satisfied: matplotlib-inline in /opt/conda/lib/python3.11/site-packages (from ipython>=6.1.0->ipywidgets<9,>=7.6->ipydatagrid->-r requirements.txt (line 19)) (0.1.6)\n",
      "Requirement already satisfied: pickleshare in /opt/conda/lib/python3.11/site-packages (from ipython>=6.1.0->ipywidgets<9,>=7.6->ipydatagrid->-r requirements.txt (line 19)) (0.7.5)\n",
      "Requirement already satisfied: prompt-toolkit!=3.0.37,<3.1.0,>=3.0.30 in /opt/conda/lib/python3.11/site-packages (from ipython>=6.1.0->ipywidgets<9,>=7.6->ipydatagrid->-r requirements.txt (line 19)) (3.0.39)\n",
      "Requirement already satisfied: pygments>=2.4.0 in /opt/conda/lib/python3.11/site-packages (from ipython>=6.1.0->ipywidgets<9,>=7.6->ipydatagrid->-r requirements.txt (line 19)) (2.16.1)\n",
      "Requirement already satisfied: stack-data in /opt/conda/lib/python3.11/site-packages (from ipython>=6.1.0->ipywidgets<9,>=7.6->ipydatagrid->-r requirements.txt (line 19)) (0.6.2)\n",
      "Requirement already satisfied: pexpect>4.3 in /opt/conda/lib/python3.11/site-packages (from ipython>=6.1.0->ipywidgets<9,>=7.6->ipydatagrid->-r requirements.txt (line 19)) (4.8.0)\n",
      "Requirement already satisfied: packaging>=17.0 in /opt/conda/lib/python3.11/site-packages (from marshmallow<4.0.0,>=3.18.0->dataclasses-json<0.7,>=0.5.7->langchain->-r requirements.txt (line 1)) (23.2)\n",
      "Requirement already satisfied: markdown-it-py>=2.2.0 in /opt/conda/lib/python3.11/site-packages (from rich<14.0.0,>=10.11.0->typer[all]<0.10.0,>=0.9.0->langchain-cli->-r requirements.txt (line 4)) (3.0.0)\n",
      "Requirement already satisfied: mypy-extensions>=0.3.0 in /opt/conda/lib/python3.11/site-packages (from typing-inspect<1,>=0.4.0->dataclasses-json<0.7,>=0.5.7->langchain->-r requirements.txt (line 1)) (1.0.0)\n",
      "Requirement already satisfied: parso<0.9.0,>=0.8.3 in /opt/conda/lib/python3.11/site-packages (from jedi>=0.16->ipython>=6.1.0->ipywidgets<9,>=7.6->ipydatagrid->-r requirements.txt (line 19)) (0.8.3)\n",
      "Requirement already satisfied: mdurl~=0.1 in /opt/conda/lib/python3.11/site-packages (from markdown-it-py>=2.2.0->rich<14.0.0,>=10.11.0->typer[all]<0.10.0,>=0.9.0->langchain-cli->-r requirements.txt (line 4)) (0.1.2)\n",
      "Requirement already satisfied: ptyprocess>=0.5 in /opt/conda/lib/python3.11/site-packages (from pexpect>4.3->ipython>=6.1.0->ipywidgets<9,>=7.6->ipydatagrid->-r requirements.txt (line 19)) (0.7.0)\n",
      "Requirement already satisfied: wcwidth in /opt/conda/lib/python3.11/site-packages (from prompt-toolkit!=3.0.37,<3.1.0,>=3.0.30->ipython>=6.1.0->ipywidgets<9,>=7.6->ipydatagrid->-r requirements.txt (line 19)) (0.2.8)\n",
      "Requirement already satisfied: executing>=1.2.0 in /opt/conda/lib/python3.11/site-packages (from stack-data->ipython>=6.1.0->ipywidgets<9,>=7.6->ipydatagrid->-r requirements.txt (line 19)) (1.2.0)\n",
      "Requirement already satisfied: asttokens>=2.1.0 in /opt/conda/lib/python3.11/site-packages (from stack-data->ipython>=6.1.0->ipywidgets<9,>=7.6->ipydatagrid->-r requirements.txt (line 19)) (2.4.0)\n",
      "Requirement already satisfied: pure-eval in /opt/conda/lib/python3.11/site-packages (from stack-data->ipython>=6.1.0->ipywidgets<9,>=7.6->ipydatagrid->-r requirements.txt (line 19)) (0.2.2)\n",
      "Note: you may need to restart the kernel to use updated packages.\n"
     ]
    }
   ],
   "source": [
    "%pip install -r requirements.txt"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "import os\n",
    "import re\n",
    "import sys\n",
    "from langchain.chat_models import AzureChatOpenAI\n",
    "from langchain.output_parsers import PydanticOutputParser\n",
    "from langchain.prompts import PromptTemplate\n",
    "from langchain.pydantic_v1 import BaseModel, Field, validator\n",
    "from langchain.tools import StructuredTool\n",
    "from typing import List\n",
    "from enum import Enum, IntEnum\n",
    "\n",
    "model =AzureChatOpenAI(deployment_name=\"gpt-4-32k\", temperature=0)\n",
    "application = \"command line fibonacci calculator\"\n",
    "technology = \"python\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Create a featurelist for the tool we want to create\n",
    "class Feature(BaseModel):\n",
    "    feature: str = Field(description=\"The feature we want to create\")\n",
    "    description: str = Field(description=\"The description of the feature we want to create\")\n",
    "\n",
    "class Featurelist(BaseModel):\n",
    "    features: List[Feature] = Field(description=\"A list of features we want to create\")\n",
    "\n",
    "\n",
    "feature_parser = PydanticOutputParser(pydantic_object=Featurelist)\n",
    "\n",
    "# Create a prompt template for the tool we want to create\n",
    "feature_prompt = PromptTemplate(\n",
    "    template=\"I want to create a {application} using {technology}. Please give a short outline of which features should be implemented. .\\n{format_instructions}\\n\",\n",
    "    input_variables=[\"application\", \"technology\"],\n",
    "    partial_variables={\"format_instructions\": feature_parser.get_format_instructions()},\n",
    ")\n",
    "\n",
    "feature_chain = feature_prompt | model | feature_parser\n",
    "\n",
    "def get_features(application: str, technology: str) -> Featurelist:\n",
    "    \"\"\"Provide a featurelist for a given application and technology\"\"\"\n",
    "    features = feature_chain.invoke({\"application\": application, \n",
    "                                    \"technology\": technology})\n",
    "    return features\n",
    "\n",
    "features = StructuredTool.from_function(get_features)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# create a directory structure for the tool we want to create\n",
    "class File(BaseModel):\n",
    "    path: str = Field(description=\"The path of the file\")\n",
    "    responsibility: str = Field(description=\"The responsibility of the file, what it should contain and what the responsibility\")\n",
    "    dependencies: List[str] = Field(description=\"The other files this file depends on\")\n",
    "\n",
    "class Files(BaseModel):\n",
    "    files: List[File] = Field(description=\"A list of files we want to create\")\n",
    "\n",
    "file_parser = PydanticOutputParser(pydantic_object=Files) \n",
    "\n",
    "\n",
    "directory_prompt = PromptTemplate(\n",
    "    template=\"I want to create a {application} using {technology} with these features: {features}. List all the files that are needed and use this list to provide a file structure for this application. Describe what each file is responsible for and include supporting files like requirements.txt, README.md and setup files when needed: .\\n{format_instructions}\\n\",\n",
    "    input_variables=[\"application\", \"technology\", \"features\"],\n",
    "    partial_variables={\"format_instructions\": file_parser.get_format_instructions()},\n",
    ")\n",
    "\n",
    "def get_directory_structure(application: str, technology: str, features: Featurelist) -> Files:\n",
    "    \"\"\"Provide a file structure for a given application, technology and Features\"\"\"\n",
    "    feature_list = ', '.join([feature.feature for feature in features.features])\n",
    "    directory_chain = directory_prompt | model | file_parser\n",
    "    directory_entries = directory_chain.invoke({\"application\": application, \n",
    "                                                \"technology\": technology,\n",
    "                                                \"features\": feature_list})\n",
    "    return directory_entries\n",
    "\n",
    "directory = StructuredTool.from_function(get_directory_structure)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# create all the files for the tool we want to create\n",
    "base_dir = os.path.join(os.getcwd(), application + \"/\")\n",
    "features = get_features(application, technology)\n",
    "feature_list = ', '.join([feature.feature for feature in features.features])\n",
    "\n",
    "directory_entries = get_directory_structure(application, technology, features)\n",
    "\n",
    "files_to_create = directory_entries.files.copy()    \n",
    "\n",
    "code_prompt = PromptTemplate(\n",
    "    template=\"I want to create a {application} using {technology} with these features: {features}. Please provide the contents for the file {file}, which is responsible for {responsibility}.  Please include inline documentation where needed. \\n\",\n",
    "    input_variables=[\"application\", \"technology\", \"file\", \"responsibility\", \"features\"],\n",
    ")\n",
    "\n",
    "code_chain = code_prompt | model\n",
    "def get_code(application: str, technology: str, file: File, features: str) -> str:\n",
    "    print(f\"Getting code for file {file.path}\")\n",
    "    code = code_chain.invoke({\"application\": application,\n",
    "                              \"technology\": technology,\n",
    "                              \"file\": file.path,\n",
    "                              \"responsibility\": file.responsibility,\n",
    "                              \"features\": features})\n",
    "    pattern = \"```(.*?)(.+)```\"    \n",
    "    result = re.search(pattern, code.content, re.DOTALL).group(2)\n",
    "\n",
    "    print(f\"Code for file {file.path} is {result}\")    \n",
    "    sys.exit()\n",
    "    return result\n",
    "\n",
    "\n",
    "def create_file(file: File):\n",
    "    print(f\"Creating file {file.path}\")\n",
    "    for dependency in file.dependencies:\n",
    "        print(f\"Checking if dependency {dependency} exists\")        \n",
    "        dependency_file = next((f for f in directory_entries.files if f.path == dependency), None)\n",
    "        print(f\"Creating dependency file {dependency_file.path} first\")\n",
    "        create_file(dependency_file)\n",
    "    if not os.path.dirname(base_dir + file.path) == \"\":\n",
    "        os.makedirs(os.path.dirname(base_dir + file.path), exist_ok=True)\n",
    "    with open(base_dir + file.path, \"w\") as f:\n",
    "        code = get_code(application, technology, file, feature_list)\n",
    "        f.write(code)\n",
    "        file_to_remove = next((f for f in files_to_create if f.path == file.path), None)\n",
    "        if file_to_remove:\n",
    "            files_to_create.remove(file_to_remove)\n",
    "\n",
    "while len(files_to_create) > 0:\n",
    "    create_file(files_to_create[0])"
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
   "display_name": "Python 3 (ipykernel)",
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
   "version": "3.11.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}