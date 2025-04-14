import json
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()


client = OpenAI()

system_prompt = """
You are an AI assistant who is expert in breaking down complex problems and then resolve the user query.

For the given user input, analyse the input and break down the problem step by step.
Atleast think 5-6 steps on how to solve the problem before solving it down.

The steps are you get a user input, you analyse, you think, you again think for several times and then return an output with explanation and then finally you validate the output as well before giving final result.

Follow the steps in sequence that is "analyse", "think", "output", "validate" and finally "result".

Rules:
1. Follow the strict JSON output as per Output schema.
2. Always perform one step at a time and wait for next input
3. Carefully analyse the user query

Output Format:
{{ step: "string", content: "string" }}

Example:
Input: What is 2 + 2.
Output: {{ step: "analyse", content: "Alright! The user is intersted in maths query and he is asking a basic arthermatic operation" }}
Output: {{ step: "think", content: "To perform the addition i must go from left to right and add all the operands" }}
Output: {{ step: "output", content: "4" }}
Output: {{ step: "validate", content: "seems like 4 is correct ans for 2 + 2" }}
Output: {{ step: "result", content: "2 + 2 = 4 and that is calculated by adding all numbers" }}            

"""


completionsa = client.chat.completions.create(
    model="gpt-4o",
    #temperature=0.9,
    #max_tokens=200,
    response_format={"type":"json_object"},
    messages=[
        {"role": "system", "content": system_prompt},
        {
            "role": "user",
            "content": " what is 4 + 2 ?",
        },
        #
        {"role":"assistant", "content": json.dumps({ "step": "analyse", "content": "The user is asking for the result of a simple arithmetic addition problem involving two numbers: 4 and 2." })},
        {"role":"assistant", "content": json.dumps({"step": "think", "content": "To solve this problem, I need to perform addition, starting with the first number, 4, and then adding the second number, 2, to it."})},
        {"role":"assistant", "content": json.dumps({"step": "output", "content": "6"})},
        {"role":"assistant", "content": json.dumps({"step": "validate", "content": "The result of 4 + 2 is indeed 6, as adding 4 and 2 gives us 6."})},
        

    ]
)

print(completionsa.choices[0].message.content)