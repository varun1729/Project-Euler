from fractions import Fraction
def isNonTrivial (a,b):
	if not((a%10 == 0) and (b%10 == 0)):
		frac = a/b
		if (frac < 1):
			numerator = list(str(a))
			denominator = list(str(b))
			for a1 in numerator:
				if (a1 in denominator):
					numerator.remove(a1)
					denominator.remove(a1)
					if ((denominator[0] != '0') and (int(numerator[0])/int(denominator[0]) == frac)):
						return True
			return False
		else:
			return False
	else:
		return False
product = 1
for x in range (10,100):
	for y in range (10,100):
		if(isNonTrivial(x,y)):
			product *b= Fraction(x,y)
			print(x,'/',y, ' ', Fraction(x,y))
print(product.denominator)

