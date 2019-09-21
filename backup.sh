print("something")

#factorial of 5
def fct(n):
	if n == 1:
		return 1
	return n*fct(n-1)

n = int(input())
print(fct(n))


