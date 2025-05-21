import requests
import base64
import datetime
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

def generate_image():
    prompt = prompt_entry.get()
    width = width_entry.get()
    height = height_entry.get()
    
    if not prompt:
        messagebox.showerror("Erro", "O campo de prompt não pode estar vazio.")
        return
    
    try:
        width = int(width)
        height = int(height)
    except ValueError:
        messagebox.showerror("Erro", "As dimensões devem ser números inteiros.")
        return

    # CORRETO: URL sem o "@cf"
    API_URL = "https://api.cloudflare.com/client/v4/accounts/9a4934d4617a5a2ee925d6c25066ea44/ai/run/stability-ai/stable-diffusion-xl"

    # Token que você forneceu
    HEADERS = {
        "Authorization": "Bearer Om1PgsZYdw9GJiRb6l_g0XrKatKPUtcB13H1QL35",
        "Content-Type": "application/json"
    }

    DATA = {
        "prompt": prompt,
        "width": width,
        "height": height
    }

    try:
        response = requests.post(API_URL, json=DATA, headers=HEADERS)
    except requests.exceptions.RequestException as e:
        messagebox.showerror("Erro de conexão", f"Erro ao conectar à API: {e}")
        return

    if response.status_code == 200:
        result = response.json()
        image_base64 = result.get("result", {}).get("image")

        if image_base64:
            timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"output_{timestamp}.png"

            try:
                with open(filename, "wb") as img_file:
                    img_file.write(base64.b64decode(image_base64))
                messagebox.showinfo("Sucesso", f"Imagem salva como {filename}")
            except Exception as e:
                messagebox.showerror("Erro", f"Erro ao salvar a imagem: {e}")
        else:
            messagebox.showerror("Erro", "Imagem não retornada pela API.")
    else:
        messagebox.showerror("Erro", f"Erro {response.status_code}: {response.text}")

# Interface gráfica com Tkinter
root = tk.Tk()
root.title("Gerador de Imagens com IA (Cloudflare)")
root.geometry("400x300")
root.configure(bg="#2C2F33")

frame = tk.Frame(root, padx=20, pady=20, bg="#2C2F33")
frame.pack(pady=10)

ttk.Style().configure("TLabel", foreground="white", background="#2C2F33", font=("Arial", 12))
ttk.Style().configure("TButton", font=("Arial", 10, "bold"))

ttk.Label(frame, text="Digite o prompt:").pack()
prompt_entry = ttk.Entry(frame, width=50)
prompt_entry.pack(pady=5)

ttk.Label(frame, text="Largura da imagem:").pack()
width_entry = ttk.Entry(frame, width=10)
width_entry.insert(0, "1024")
width_entry.pack(pady=5)

ttk.Label(frame, text="Altura da imagem:").pack()
height_entry = ttk.Entry(frame, width=10)
height_entry.insert(0, "1024")
height_entry.pack(pady=5)

generate_button = ttk.Button(frame, text="Gerar Imagem", command=generate_image)
generate_button.pack(pady=10)

root.mainloop()
