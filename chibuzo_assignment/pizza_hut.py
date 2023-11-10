def box_size(size: str):
    pizza_boxes = {"SMALL": 4, "MEDIUM": 6, "LARGE": 10}
    size = size.upper()
    if size in pizza_boxes.keys():
        return pizza_boxes.get(size)


def number_of_hungry_persons(super_hungry: int, normal_hungry: int, classic_hungry):
    persons = (super_hungry * 4 + normal_hungry * 2 + classic_hungry * 1)

    return persons


def number_of_slices(super_hungry: int, normal_hungry: int, classic_hungry):
    slices = (super_hungry * 4 + normal_hungry * 2 + classic_hungry * 1)
    persons = 0
    if slices == persons:
        slices = persons

    return slices


def number_of_boxes(super_hungry: int, normal_hungry: int, classic_hungry, box=None):
    small_boxes = (super_hungry * 4 + normal_hungry * 2 + classic_hungry * 1) / 4
    medium_boxes = (super_hungry * 4 + normal_hungry * 2 + classic_hungry * 1) / 6
    large_boxes = (super_hungry * 4 + normal_hungry * 2 + classic_hungry * 1) / 10

    if box == 4:
        box = small_boxes
    elif box == 6:
        box = medium_boxes
    elif box == 10:
        box = large_boxes

    return box


def number_of_slices_remaining(super_hungry: int, normal_hungry: int, classic_hungry, box=None):
    small_boxes = (super_hungry * 4 + normal_hungry * 2 + classic_hungry * 1) % 4
    medium_boxes = (super_hungry * 4 + normal_hungry * 2 + classic_hungry * 1) % 6
    large_boxes = (super_hungry * 4 + normal_hungry * 2 + classic_hungry * 1) % 10

    if box == 4:
        box = small_boxes
    elif box == 6:
        box = medium_boxes
    elif box == 10:
        box = large_boxes

    return box


def boxes_total_amount(super_hungry: int, normal_hungry: int, classic_hungry, slice=None):
    small_box = (super_hungry * 4 + normal_hungry * 2 + classic_hungry * 1) / 4
    medium_boxes = (super_hungry * 4 + normal_hungry * 2 + classic_hungry * 1) / 6
    large_boxes = (super_hungry * 4 + normal_hungry * 2 + classic_hungry * 1) / 10

    if slice == 4:
        box = small_box * 1200
    elif slice == 6:
        box = medium_boxes * 3000
    elif slice == 10:
        box = large_boxes * 5000

    return box
