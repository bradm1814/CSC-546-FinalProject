import requests

def call_llm(prompt, system="", model="mistral"):

    payload = ({
        "model": model,
        "prompt": prompt,
        "system": system,
        "stream": False
    })

    response = requests.post("http://localhost:11434/api/generate", json=payload)
    return response.json()["response"]