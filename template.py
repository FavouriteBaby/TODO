#coding=utf-8
import calendar

class Template:
	def __init__(self, year, month):
		self.year = year
		self.month = month
		self.path = ""
		self.text = ""

	def createFile(self):
		days = calendar.monthrange(self.year, self.month)[1]

		self.path = str(self.year) + "-" + str(self.month) + ".org"
		print(self.path)
		smallTitle = "** TODO Study\n\n** TODO Work\n\n** TODO Life\n\n"
		title = ""
		text = ""
		for day in range(1,days+1):
			bigTitle = "* " + str(self.year) + "-" + str(self.month) + "-" + str(day) + " [%]\n\n"
			title = bigTitle + smallTitle
			text += title

		with open(str(self.path), "a") as f:
			f.write(str(text))
		f.close()

if __name__ == '__main__':
	year = raw_input("Year:")
	month = raw_input("Month:")
	template = Template(int(year), int(month))
	template.createFile()
