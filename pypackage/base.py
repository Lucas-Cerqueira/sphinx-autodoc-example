"""
Defines the base class.
"""


class BaseClass:
    """Base class.

    Parameters
    ----------
    x : int
        Parameter `x` description.
    y : str, default="abcd"
        Parameter `y` description.
    """
    def __init__(self, x, y="abcd"):
        self.x = x
        self.y = y

    def x_squared(self):
        """Returns the value of the attribute `x` squared.

        Returns
        -------
        int
            Value of the attribute `x` squared.
        """
        return self.x ** 2



def clone(base_obj):
    """Clones a `BaseClass` instance and returns the copy.

    Parameters
    ----------
    base_obj : object
        BaseClass instance to be cloned.

    Returns
    -------
    clone : :class:`base.BaseClass <pypackage.base.BaseClass>`
        A clone of `base_obj`.

    """
    return BaseClass(base_obj.x, base_obj.y)
