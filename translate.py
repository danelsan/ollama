import requests
import json
import sys

def query_ollama_mistral(prompt):
    url = "http://localhost:11434/api/generate"  # Assicurati che l'URL e la porta siano corretti
    headers = {
        "Content-Type": "application/json"
    }
    payload = {
        "model": "mistral",
        "prompt": prompt,
        "stream": False
    }
    response = requests.post(url, json=payload, headers=headers)
    return response.json()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 translate_ollama_mistral.py <input_file>")
        sys.exit(1)

    input_file = sys.argv[1]

    # Leggi il testo dal file di input
    with open(input_file, "r") as file:
        text_to_translate = file.read().strip()

    # Crea il prompt per la traduzione in italiano
    prompt = f"Dammi sono la traduzione in italiano: {text_to_translate}"

    # Query al modello Mistral di Ollama
    result = query_ollama_mistral(prompt)

    # Stampa solo il valore della chiave 'response'
    if 'response' in result:
        print(result['response'])
    else:
        print("La risposta non contiene la chiave 'response'")

