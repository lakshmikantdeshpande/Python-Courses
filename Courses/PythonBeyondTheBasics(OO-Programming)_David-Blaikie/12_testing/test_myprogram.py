# Use py.test to run the tests in the current directory
# USAGE: py.test 

import pytest
import myprogram

def test_doubleit():
	assert myprogram.doubleit(10) == 20


def test_doubleit_type():
	with pytest.raises(TypeError):
		myprogram.doubleit('5adsfsdf')

