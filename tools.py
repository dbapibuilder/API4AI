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


# Map the tool names to the functions on openai assistant control console
TOOL_MAP = {"get_weather": get_weather,
            "search_internet": search_internet,
            "send_email": send_email,
            "generate_image": generate_image

            }
