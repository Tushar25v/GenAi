import tiktoken

encode = tiktoken.encoding_for_model("gpt-4o")

#print("vocab_size", encode.n_vocab)

text = "Tushar is the gretest of all time"

tokens= encode.encode(text)   #tokens [51, 1776, 277, 382, 290, 3727, 3190, 328, 722, 1058]

#print("tokens", tokens)


my_tokens = [51, 1776, 277, 382, 290, 3727, 3190, 328, 722, 1058]

decodeded = encode.decode(my_tokens)

print("decoded message:", decodeded)