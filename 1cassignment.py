n = 30563323
d = 3
def recurCountDigit(n,d):
	if n == 0:
		return 0
	lastDigit = n % 10
	if lastDigit == d:
		return 1 + recurCountDigit(n // 10, d)
	else:
		return recurCountDigit(n//10, d)

occurr = recurCountDigit(n, d)
print(f"The digit {d} occurs {occurr} times in the number {n}.")