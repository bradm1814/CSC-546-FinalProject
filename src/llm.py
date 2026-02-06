import requests

def call_mistral(prompt, system="", model="mistral"):

    payload = ({
        "model": model,
        "prompt": prompt,
        "system": system,
        "stream": False
    })

    response = requests.post("http://localhost:11434/api/generate", json=payload)
    return response.json()["response"]


def call_sqlcoder(prompt, model="sqlcoder:15b"):

    payload = ({
        "model": model,
        "prompt": prompt,
        "stream": False
    })

    response = requests.post("http://localhost:11434/api/generate", json=payload).json()

    if "response" in response:
        return response["response"]
    if "output" in response:
        return response["output"]

    return str(response)