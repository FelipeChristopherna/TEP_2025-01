import requests
import base64
import datetime

# API info
API_URL = "https://api.cloudflare.com/client/v4/accounts/9a4934d4617a5a2ee925d6c25066ea44/ai/run/black-forest-labs/flux-1-schnell"
HEADERS = {
    "Authorization": "Bearer ooe5ErPspRCmhLUmVuxyZEXftX--9HHcIaPCFrdd",
    "Content-Type": "application/json"
}

def gerar_imagem(prompt: str, seed: int = None):
    data = {
        "prompt": prompt
    }

    if seed is not None:
        data["seed"] = seed

    response = requests.post(API_URL, headers=HEADERS, json=data)

    if response.status_code == 200:
        result = response.json()
        imagem_base64 = result.get("result", {}).get("image")

        if imagem_base64:
            nome_arquivo = f"imagem_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.jpg"
            with open(nome_arquivo, "wb") as f:
                f.write(base64.b64decode(imagem_base64))
            print(f"✅ Imagem salva como: {nome_arquivo}")
        else:
            print("⚠️ Nenhuma imagem retornada.")
    else:
        print(f"❌ Erro {response.status_code} - {response.text}")

# ----------------------------------
# Exemplo de uso
prompt = "a cyberpunk dragon flying over neon city"
gerar_imagem(prompt)
