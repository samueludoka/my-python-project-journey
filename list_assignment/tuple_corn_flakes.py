def reverse_list(numb):
    num = (10, 20, 30, 40, 50)
    new_num = ()
    for k in range (len(numb)):
        new_num = new_num + (numb[-k -1],)

    return new_num

def get_integer(list):
    num = ("orange", [10, 20, 30], (5, 15, 25))
    lio = num[1][1]
    kio = num[2][2]
    sal = ((1, lio), (2, kio))

    return sal


def offload_element(number):
    numb = (15, 25, 60, 50, 30, 40, 45, 55)
    pal = numb[0]
    gal = numb[7]
    big = (gal, pal)

    return big


def rearrange_list(list):
    number = (('a', 23), ('b', 37), ('c', 11), ('d', 29))
    bef = (('c', 11), ('a', 23), ('d', 29), ('b', 37))

    return bef


def duplicate(numbers):
    number = 20, 10, 15, 20, 5, 30, 10, 35, 10, 40, 45, 5
    set(number)

