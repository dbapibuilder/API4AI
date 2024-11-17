import json
import requests
import os
from dotenv import load_dotenv

load_dotenv()

TOOLS_API_GATEWAY_URL = os.getenv("TOOLS_API_GATEWAY_URL")
TOOLS_API_GATEWAY_KEY = os.getenv("TOOLS_API_GATEWAY_KEY")


def get_weather(location: str):
    
    reqUrl = TOOLS_API_GATEWAY_URL + "/v1/weather"

    headersList = {
    "Content-Type": "application/json",
    "Authorization": TOOLS_API_GATEWAY_KEY
    }

    payload = json.dumps({"location":location})

    response = requests.request("POST", reqUrl, data=payload,  headers=headersList)

    return json.dumps(response.json())



def search_internet(query: str):
    reqUrl = TOOLS_API_GATEWAY_URL + "/v1/internet"

    headersList = {
    "Content-Type": "application/json",
    "Authorization": TOOLS_API_GATEWAY_KEY 
    }

    payload = json.dumps({"query":query})

    response = requests.request("POST", reqUrl, data=payload,  headers=headersList)

    return response.text


def send_email(to: str, subject: str, content: str):
    reqUrl = TOOLS_API_GATEWAY_URL + "/v1/email"

    headersList = {
    "Content-Type": "application/json",
    "Authorization": TOOLS_API_GATEWAY_KEY 
    }

    payload = json.dumps({"to":to, "subject":subject, "content":content})

    response = requests.request("POST", reqUrl, data=payload,  headers=headersList)

    return response.text

def generate_image(prompt: str):
    reqUrl = TOOLS_API_GATEWAY_URL + "/v1/image"

    headersList = {
    "Content-Type": "application/json",
    "Authorization": TOOLS_API_GATEWAY_KEY 
    }

    payload = json.dumps({"prompt":prompt})

    response = requests.request("POST", reqUrl, data=payload,  headers=headersList)

    return response.text


def search_arxiv(search_query: str):
    """
    Retrieve academic papers from the ArXiv database.
    
    This function sends a GET request to a Zuplo gateway which forwards the request to the ArXiv API.
    The search_query parameter can include all necessary query parameters in ArXiv API format.

    Parameters:
    - search_query (str): A string representing the ArXiv query. This can include:
        - Search terms (with or without field prefixes like ti:, au:, etc.)
        - Additional query parameters like start, max_results which are part of the URL query string.

    Returns:
    - str: The response text from the ArXiv API.

    Example usage:
    >>> search_arxiv("au:del_maestro")
    >>> search_arxiv("all:electron&start=0&max_results=10")
    >>> search_arxiv("all:electron+AND+all:proton")
    """
    reqUrl = TOOLS_API_GATEWAY_URL + "/v1/arxiv"
    headersList = {
        "Authorization": TOOLS_API_GATEWAY_KEY
    }
    
    # The search_query includes all parameters, so we just append it to the URL
    full_url = f"{reqUrl}?search_query={search_query}"
    
    response = requests.request("GET", full_url, headers=headersList)
    return response.text


# Map the tool names to the functions on openai assistant control console
TOOL_MAP = {"get_weather": get_weather,
            "search_internet": search_internet,
            "send_email": send_email,
            "generate_image": generate_image,
            "search_arxiv": search_arxiv

            }
