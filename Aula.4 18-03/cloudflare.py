import requests


API_BASE_URL = "https://api.cloudflare.com/client/v4/accounts/9a4934d4617a5a2ee925d6c25066ea44/ai/run/"
headers = {"Authorization": "Bearer Om1PgsZYdw9GJiRb6l_g0XrKatKPUtcB13H1QL35"}


def run(model, inputs):
    input = { "messages": inputs }
    response = requests.post(f"{9a4934d4617a5a2ee925d6c25066ea44}{model}", headers=headers, json=input)
    return response.json()


inputs = [
    { "role": "system", "content": "You are a friendly assistan that helps write stories" },
    { "role": "user", "content": "Write a short story about a llama that goes on a journey to find an orange cloud "}
];
output = run("@cf/meta/llama-3-8b-instruct", inputs)
print(output)