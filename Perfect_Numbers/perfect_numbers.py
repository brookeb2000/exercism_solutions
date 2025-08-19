def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    try:
        num = float(number)
    except ValueError:
        raise ValueError("input must be a number")

    if num != int(num) or num <= 0:
        raise ValueError("Classification is only possible for positive integers.")

    aliquot_sum = 0
    for i in range(1, number):
        if number % i == 0:
            aliquot_sum += i
    if aliquot_sum == number:
        return "perfect"
    if aliquot_sum > number:
        return "abundant"
    return "deficient"