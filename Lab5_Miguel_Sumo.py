"""
Miguel Sumo
Lab 5
2/10/23
"""



def main():


	
	#x = "tx33dom"
	#x = "t3xb3f"
	#x = "koxb3zpond3nk3"
	#x = "fako fim3"
	#x = "zom3 xafz bun"	
	#x = "txiday tun tob tx3nkh tbi3z"
	#x = "kafz kan kafkh kakfuz3z wifh klawz"
	
	
	
	x = "UUHO"  		#Used for Bonus
	#encodedWord = "EOUUUUOUU" 	#Used for Bonus
	
	print(DecodeWord(x))






#Your code goes here.
def DecodeWord(x):
	z=''
	i=int(0)
	for i in range(len(x)):
		if x[i]=="t":
			z+='f'
		elif x[i]=="f":
			z+='t'
		elif x[i]=="3":
			z+='e'
		elif x[i]=="k":
			z+='c'
		elif x[i]=="z":
			z+='s'
		elif x[i]=="b":
			z+='r'
		elif x[i]=="x":
			z+='r'
		else:
			z+=x[i]	
	return(z)












#This code triggers the main to run
#we'll talk about this more in chapters 6,7, & 8.	
if __name__ == "__main__":
	main()
