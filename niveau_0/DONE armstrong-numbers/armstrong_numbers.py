def is_armstrong(num):
	digitLength = len(str(num))
	sum = 0
	tempNum = num
	while tempNum > 0:
	   digit = tempNum % 10
	   sum += digit ** digitLength
	   tempNum //= 10

	return True if num == sum else False
