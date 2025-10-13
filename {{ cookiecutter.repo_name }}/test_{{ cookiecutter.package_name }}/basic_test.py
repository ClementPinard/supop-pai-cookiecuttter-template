import numpy as np
import {{ cookiecutter.package_name }}

def test_typed_function():
    assert {{ cookiecutter.package_name }}.typed_function(np.zeros(10), "") == False