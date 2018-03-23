import urlify

def test_unit(self):
	"""docstring for test_unit"""
	dat = [
			(list('much ado about nothing      '), 22,
				list('much%20ado%20about%20nothing')),
			(list('Mr John Smith    '), 13,
				list('Mr%20John%20Smith'))
			]
	for [test_string, length, expected] in self.data:
		actual = urlif(test_string,length)
		self.assertEqual(actual, expected)
