import re
#bir dizeden maksimum sayı değerini çıkartan algoritma
def extractMax(input):

	numbers = re.findall('\d+',input)

	numbers = map(int,numbers)

	print (max(numbers))

if __name__ == "__main__":

	input = '100klh564abc365bg'

	extractMax(input)