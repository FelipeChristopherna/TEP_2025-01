import os

from groq import Groq

client = Groq(
    api_key=os.environ.get("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"),
)

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "Explain the importance of fast language models",
        }
    ],
    model="llama-3.3-70b-versatile",
)

print(chat_completion.choices[0].message.content)