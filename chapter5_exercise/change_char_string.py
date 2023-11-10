

def dolapo(words: str, new_String: str, old_String: str):
    first_letter = words[0]
    words = words.replace(old_String, new_String)
    return first_letter + words[1:]


print(dolapo('restart', '$', 'r'))
