import warnings

citation = {
        'journal'      : 'The Mathematical Intelligencer',
        'volume'       : 38,
        'number'       : 1,
        'season'       : 'Spring',
        'year'         : 2016,
        'title'        : 'Prague Clocks',
        'first_author' : 'Chan Bae',
    }


def triangular_num_list(n):
    """
    finds the first n triangular numbers
    """
    num_list = []
    cumulative = 0
    for num in range(n):
        cumulative = cumulative + num
        num_list.append(cumulative)
    return num_list


def modulo_list(modulo, num_list=None, append_m=True):
    """
    reduces the first modulo-1 triangular numbers mod modulo
    """
    if num_list is None:
        num_list = triangular_num_list(modulo)
    num_list = sorted(set(num % modulo for num in num_list))
    if append_m:
        num_list.append(modulo)
    return num_list


def sorted_list_diff(modulo=None, num_list=None):
    """
    sorts and calculates differences given a modulo
    """
    if modulo is not None:
        if num_list is not None:
            warnings.warn('num_list argument overwridden by modulo argument')
        num_list = modulo_list(modulo)
    num_list = sorted(num_list)
    diff_list = []
    for i in range(1, len(num_list)):
        diff_list.append(num_list[i] - num_list[i - 1])
    return diff_list


        