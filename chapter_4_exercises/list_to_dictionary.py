def last_to_dictionary(score):
    for num in score:
        for numb in num:
            if numb in num[0] == 0:
                break

    return {num[0]: num}


def two_list_to_dictionary(word: str, score: int):
    for i in word:
        pass
    for j in score:
        pass
    return {i: j}


# print(two_list_to_dictionary(['a', 'b', 'C', 'd', 'e'],[1, 2, 3, 4, 5]))


def difference_in_smallest_and_largest_in_a_list(score):
    min = 0,
    max = 0
    for i in score:
        if i > max == 0:
            max = i
        elif i < min == 0:
            min = i

    return max - min


def frequency(scores):
    score = []
    for x in scores:
        if x >= 2 == 0:
            score.append(x)

    return score


def remove_multiple_String(word):
    for x in word:
        for y in x:
            pass

    return ['y', x[1], x[2]]


def split_a_list(word):
    sample_input = (len(word))
    score = []
    word = []
    count = 0
    for y in range(len(word)):
        while y != sample_input[5]:
            score.append(y)
            count += 1

        while y == sample_input[5]:
            word.append(y)
            count += 1

    return score, word
