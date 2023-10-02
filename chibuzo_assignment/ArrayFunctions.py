def listLargest(scores):
    largest_number = 0
    for i in scores:
        if i > largest_number:
            largest_number = i
    return largest_number


def reverse_a_list(scores):
    convert = []
    for i in scores[::-1]:
        convert.append(i)
    return convert


def odd_number_in_a_list(scores):
    odd = []
    for i in scores[::+2]:
        odd.append(i)
    return odd


def even_number_in_a_list(scores):
    even = []
    for i in scores[1::+2]:
        even.append(i)

    return even


def element_exist_in_a_list(scores):
    element = [scores]
    element2 = {3}

    return element2


def running_total(scores):
    total = 0
    for i in scores:
        total += i
    return total


def stringPalindrome(lists):
    return lists == lists[::-1]


def totalOfList(scores):
    total = 0
    for i in scores:
        total = total + i

    return total


def totalOfList2(scores):
    total = 0
    count = 0
    while count < scores:
        count += 1
        total = total + count
    return total


def concatenate(scores: int, scores1: str):
    list = []
    for i in scores:
        list.append(i)
    for a in scores1:
        list.append(a)
    return list

def combine_two_list(first_list, second_list):
    list = []
    count = 0
    for i in first_list:
        list.append(i)
        list.append(second_list[count])
        count += 1
    return list