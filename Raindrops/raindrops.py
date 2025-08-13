def convert(number):
    """
    gives the corresponding raindrop sounds to a given number:
    -if divisible by 3, "Pling" added to the result
    -if divisible by 5, "Plang" added to the result.
    -if divisible by 7, "Plong" added to the result.
    -if not divisible by 3, 5, or 7, result will be the number as a string.
    param number: int
    return: string, the raindrop sounds
    """
    raindrop_sound = str()
    if number % 3 == 0:
        raindrop_sound += "Pling"
    if number % 5 == 0:
        raindrop_sound += "Plang"
    if number % 7 == 0:
        raindrop_sound += "Plong"
    if raindrop_sound == "":
        raindrop_sound += str(number)
    return raindrop_sound
