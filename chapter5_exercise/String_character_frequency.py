def character_frequency(word: str):
    result = {}
    for num in word:
        if num in result.keys():
            result[num] += 1
        else:
            result[num] = 1

    return result


print(character_frequency("bible"))


def character_frequency2(words: str):
    return {word: words.count(word) for word in words}


print(character_frequency2("google.com"))
