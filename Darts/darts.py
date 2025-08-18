def score(x, y):
    """Based on darts x,y location, returns the score recieved.

    :param x: any real number, x-coordinate of dart
    :param y: any real number, y-coordinate of dart
    :return: int - the score recieved
    """
    outer_radius = 10
    middle_radius = 5
    inner_radius = 1
    distance = x*x + y*y
    if distance <= inner_radius*inner_radius:
        return 10
    if distance > inner_radius*inner_radius and distance <= middle_radius*middle_radius:
        return 5
    if distance > middle_radius*middle_radius and distance <= outer_radius*outer_radius:
        return 1
    return 0