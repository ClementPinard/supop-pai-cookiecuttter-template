"""This module serves as a basis for your project. You can either use NiceGUI
or Pyside to start.

The project assumes that your main entrypoint is the function run() of this file
(see pyproject.toml scripts)
"""

import numpy as np


def type_function(a: np.ndarray, b: str = "") -> bool:
    """This is a typed function.
    This docstring is made so that it renders nicely on sphinx. It features notes,
    arguments, cross references (here, to numpy documentation), maths and examples.

    Notes:
        - This is a section with multiple notes
        - This second note has maths! :math:`p \in \mathbb{N}`

    .. math::
        :label: equation1

        D = \sum_{0 \le i < p} \alpha_i

    Args:
        a: first parameter, its description is really, and fits in
            two lines (note the indentation). The object must be a :obj:`np.ndarray`
        b: second parameter. Defaults to empty string.

    Examples
        >>> type_function(np.zeros(10))
        False
        >>> type_function(
        ...     np.zeros(10),
        ...     "hello"
        ... )
        False

    Returns:
        Always return False, it's not a very interesting function. See :eq:`equation1`
        for some more maths.
    """
    return False


def run():
    """This is the main function that gets run"""
