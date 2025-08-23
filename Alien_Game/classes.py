"""Solution to Ellen's Alien Game exercise."""


class Alien:
    """Create an Alien object with location x_coordinate and y_coordinate.

    Attributes
    ----------
    (class)total_aliens_created: int
    x_coordinate: int - Position on the x-axis.
    y_coordinate: int - Position on the y-axis.
    health: int - Number of health points.

    Methods
    -------
    hit(): Decrement Alien health by one point.
    is_alive(): Return a boolean for if Alien is alive (if health is > 0).
    teleport(new_x_coordinate, new_y_coordinate): Move Alien object to new coordinates.
    collision_detection(other): Implementation TBD.
    """
    total_aliens_created = 0
    def __init__(self, x_coord, y_coord):
        self.health = 3
        self.x_coordinate = x_coord
        self.y_coordinate = y_coord
        Alien.total_aliens_created += 1

    def hit(self):
        self.health -= 1

    def is_alive(self):
        if self.health <= 0:
            return False
        return True

    def teleport(self, x_coord, y_coord):
        self.x_coordinate = x_coord
        self.y_coordinate = y_coord
    def collision_detection(self, other_object):
        pass


def new_aliens_collection(positions):
    alien_list = []
    for coordinate in positions:
        new_alien = Alien(coordinate[0], coordinate[1])
        alien_list.append(new_alien)
    return alien_list
    