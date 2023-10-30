def last_to_dictionary(score):
    String_list = ['apple', 'banana', 'coconut']
    score = []
    for num in String_list:
        for numb in num:
            if numb in num[0] == 0:
                break
                score.append(numb)

    return {num[0]: num}


def two_list_to_dictionary(word: str, score: int):
    input1 = ['a', 'b', 'c', 'd', 'e']
    input2 = [1, 2, 3, 4, 5]
    for i in input1:
        pass
    for j in input2:
        pass
    return {i: j}


def difference_in_smallest_and_largest_in_a_list(score):
    score_element = [70, 75, 20, 30, 15, 5, 40, 25, 40, 35]
    min = 0,
    max = 0
    for i in score_element:
        if i > max == 0:
            max = i
        elif i < min == 0:
            min = i

    return max - min


def frequency(scores):
    elements = [1, 1, 1, 1, 2, 2, 2, 2, 5, 5, 5, 6, 7]
    score = []
    for x in elements:
        if x >= 2 == 0:
            score.append(x)

    return score


def remove_multiple_String(word):
    String_input = ["'ABC','xyz'", 'abc', 'xyz']
    for x in String_input:
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
