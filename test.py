class test:

	def __init__(self):
		self.name = 'wat'

	@staticmethod
	def create():
		return test()

def main():
	test_class =  test.create()
	print(test_class.name)

main()