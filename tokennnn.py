import tiktoken

encode = tiktoken.encoding_for_model("gpt-4o")

text = "Tushar is the greatest of all time"
tokens = encode.encode(text)

my_tokens = [51, 1776, 277, 382, 290, 3727, 3190, 328, 722, 1058]
decoded = encode.decode(my_tokens)

print("Decoded message:", decoded)