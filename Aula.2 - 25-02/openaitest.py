from openai import OpenAI
client = OpenAI()

completion = client.chat.completions.create(
    model = "gpt-4o-mini",
    messages = [
        {"role": "system", "content": "Você é um dono de uma tabacaria."},
        {"role": "user", "content": "Me recomende os melhores mix de rosh para um dia quente!"},
    ]
)


print(completion.choices[0].message.content)