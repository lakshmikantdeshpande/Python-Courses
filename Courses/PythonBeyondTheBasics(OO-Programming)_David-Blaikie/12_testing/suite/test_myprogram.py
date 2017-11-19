# Use py.test to run the tests in the current directory
# USAGE: py.test 

import pytest
import shutil
import os
import myprogram

class TestDoubleit(object):

	numbers_file_template = 'testnums_template.txt'
	numbers_file_tester = 'testnums.txt'
	
	def setup_class(self):
		shutil.copy(TestDoubleit.numbers_file_template, TestDoubleit.numbers_file_tester)

	def test_doublelines(self):
		myprogram.doublelines(TestDoubleit.numbers_file_tester)
		old_vals = [int(line) for line in open(TestDoubleit.numbers_file_template)]
		new_vals = [int(line) for line in open(TestDoubleit.numbers_file_tester)]

	def test_doubleit_value(self):
		assert myprogram.doubleit(10) == 20


	def test_doubleit_type(self):
		with pytest.raises(TypeError):
			myprogram.doubleit("Hello")

