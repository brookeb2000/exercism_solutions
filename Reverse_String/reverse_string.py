def reverse(text):
    """Takes a string and returns the string reversed
    :param text: string
    :return: string the reversed string
    """
    if not isinstance(text, str):
        raise TypeError("Input must be a string")
    string = "" 
    for char in reversed(text):
        string += char
    return string