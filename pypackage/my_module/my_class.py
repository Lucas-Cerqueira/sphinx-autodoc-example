from ..base import BaseClass


class MyClass(BaseClass):
    """My custom class.

    Parameters
    ----------
    w : float
        Description of `w`.
    """
    def __init__(self, w):
        super().__init__(0, "xyz")
        self.w = w

    def round(self):
        """Returns the attribute `w` rounded to integer.

        Returns
        -------
        int
            The attribute `w` rounded to integer.
        """
        return round(self.w)

    def lower(self):
        """Returns the attribute `y` in lowercase.

        Returns
        -------
        str
            The attribute `y` in lowercase.
        """
        return self.y.lower()

    def upper(self):
        """Returns the attribute `y` in uppercase.

        Returns
        -------
        str
            The attribute `y` in uppercase.
        """
        return self.y.upper()
