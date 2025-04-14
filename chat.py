from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()


client = OpenAI()





completionsa = client.chat.completions.create(
    model="gpt-3.5-turbo",
    temperature=0.9,
    max_tokens=100,
    messages=[
        {"role": "developer", "content": "Talk like a trump."},
        {
            "role": "user",
            "content": "what is life",
        },

    ]
)

print(completionsa.choices[0].message.content)