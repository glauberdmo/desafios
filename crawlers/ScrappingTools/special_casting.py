def string_to_int_with_k(str_number:str)->int:
    """
    This function convert a string number to int number with k.
    :param str_number: string number
    :return: int number
    """
    if str_number == '•':
        str_number = 0 
    if str_number.endswith('k'):
        str_number = str_number[:-1]
        return int(str_number.replace('.', '')) * 100
    else:
        return int(str_number)