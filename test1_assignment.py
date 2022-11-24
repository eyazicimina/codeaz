
class Teacher:
	isim = None
	numara = None
	fenn = None

	def __init__(self, name, number, subject):
		self.isim = name
		self.numara = number
		self.fenn = subject

	# magic function
	def __str__(self):
		return self.isim + ":" + self.fenn

"""
t = Teacher()
t.isim = "Emre"
t.numara = 344
t.fenn = "data science"
print(t)
"""

t = Teacher("Emre", 344, "data science")
print(t)
