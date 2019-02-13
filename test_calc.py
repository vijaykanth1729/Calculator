import calc
class Test:
	def test_add(self):
		assert 4 == calc.add(2,2)
	def test_sub(self):
		assert 9 == calc.sub(18,9)



#pytest -v --cov