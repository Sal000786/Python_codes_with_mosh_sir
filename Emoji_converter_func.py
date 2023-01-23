def Emoji_converter(message):
    out=message.split(" ")
    emojis={
        '):': "🙂",
        ":(": "😒"
    }
    output=" "
    for word in out:
        output+=emojis.get(word,word)+" "
    return output


message=input("> ")
print(Emoji_converter(message))
print("finished!")