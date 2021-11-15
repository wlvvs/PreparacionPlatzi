from icecream import ic

def remove_duplicates(some_list):
    without_duplicates = []
    for element in some_list:
        if element not in without_duplicates:
            without_duplicates.append(element)
    return without_duplicates


def remove_duplicates_set(some_list):
    return list(set(some_list))


def run():
    random_list = [1, 2, 3, 4, 6, 7, 8, 10, 1, 2, 3, 4, 5, 6, 7, 1, 2, 3, 4, 5]
    ic(random_list)
    ic(remove_duplicates(random_list))
    ic(remove_duplicates_set(random_list))


if __name__ == '__main__':
    run()