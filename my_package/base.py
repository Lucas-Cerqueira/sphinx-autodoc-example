"""
Defines the vehicle base class.
"""


class Vehicle:
    """Vehicle base class.

    Parameters
    ----------
    wheel_count : int
        Vehicle's wheel count.
    hp : int
        Vehicle's power in horsepower.
    weight : int or float
        Vehicle's weight in kilograms.
    """
    def __init__(self, wheel_count, hp, weight):
        self.wheel_count = wheel_count
        self.hp = hp
        self.weight = weight

    def set_wheel_count(self, wheel_count):
        """Set the vehicle's wheel count.

        Parameters
        ----------
        wheel_count : int
            Vehicle's new wheel count.

        Returns
        -------
        None
            Nothing is returned.
        """
        self.wheel_count = wheel_count

    def set_hp(self, hp):
        """Set the vehicle's horsepower.

        Parameters
        ----------
        hp : int
            Vehicle's new power in horsepower.

        Returns
        -------
        None
            Nothing is returned.
        """
        self.hp = hp

    def set_weight(self, weight):
        """Set the vehicle's weight.

        Parameters
        ----------
        weight : int or float
            Vehicle's new weight.

        Returns
        -------
        None
            Nothing is returned.
        """
        self.weight = weight


def clone(vehicle):
    """Clones a `Vehicle` instance and returns the copy.

    Parameters
    ----------
    vehicle : object
        Vehicle instance to be cloned.

    Returns
    -------
    clone : :class:`base.Vehicle <my_package.base.Vehicle>`
        A clone of `vehicle`.

    """
    return Vehicle(vehicle.wheel_count, vehicle.hp, vehicle.weight)
