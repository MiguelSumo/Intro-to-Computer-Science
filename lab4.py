#Miguel Sumo 2/3/23
#Input#
bound=int(input("Enter an upper bound for a check?:"))
div=0
perfect=0
deficient=0
abundant=0
for check in range(1,bound+1):
	for x in range(1,check):
		if check%x==0:
			div=div+x
	if div==check:
		perfect+=1
	if div<check:
		deficient+=1
	if div> check:
		abundant+=1
	div=0
print(perfect,"perfect numbers")
print(deficient,"deficient numbers")
print(abundant,"abundant numbers")
