import isUnique

def test_unit():
	"""docstring for test_unit"""
	data = [
			("yes", True),
			("blah", True),
			("words", True),
			("bb", False),
			("yaa", False),
			("dd", False),
			("yy", False)
			]
	for [test_string ,expected] in data:
		actual = isUnique.is_Unique(test_string)
		assert actual ==  expected
