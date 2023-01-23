message=input("> ")
out=message.split(" ")
# print(out)
emojis={
    '):': "🙂",
    ":(": "😒"
}
output=" "
# for x in message:
    # pass
#     output+=x
#     # out[-1]=out.append(emojis["):"])
# for out[-1] in emojis:
#     output+=emojis[out[-1]]
# print(output)
    # output+=message+ emojis[x]
#     if out[-1] in emojis:
#         message=message.replace(out[-1],emojis.get(x))
#         # print(message)

# print(message)

# if out[-1] in emojis:
#     for x in out[-1]:
#         message=message.replace(out[-1],emojis.get(x))
# print(message)



for word in out:
    output+=emojis.get(word,word)
print(output)