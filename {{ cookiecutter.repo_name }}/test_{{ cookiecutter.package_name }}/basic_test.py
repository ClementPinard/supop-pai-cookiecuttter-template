import numpy as np
from {{ cookiecutter.package_name }}.my_module import typed_function

def test_typed_function():
    assert typed_function(np.zeros(10), "") == False
