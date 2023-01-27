#Miguel Sumo
#Lab3
#1/27/23@1:00 pm

#Taking Inputs#
status=input("Are you a Senior or Junior associate?:")
sales=input("What was your sales amount?:")
sales=int(sales)
#Calculations & Outputs
if status=="Senior":
	#Senior Bonus#
	clients=input("How many new clients have you brought in?:")
	clients=int(clients)
	bonus=clients*500
	if sales<=5000 and sales>=1:
		print("your commision is",sales*.04+bonus)
	elif sales>=5001 and sales<=25000:
		x=(sales-5000)
		print("your commision is",(5000*.04)+(x*.05)+bonus)
	elif sales>=25001 and sales<=100000:
		y=(sales-25000)
		print("your commision is",(5000*.04)+(20000*.05)+(y*.07)+bonus)
	elif sales>=100000:
		z=(sales-100000)
		print("your commision is",(5000*.04)+(20000*.05)+(75000*.07)+(z*.1)+bonus)
	elif sales<=0:
		print("Head to HR")
#Junior#		
if status=="Junior":
	if sales<=5000 and sales>=1:
		print("your commision is",sales*.03)
	elif sales>=5001 and sales<=25000:
		x=(sales-5000)
		print("your commision is",(5000*.03)+(x*.04))
	elif sales>=25001 and sales<=100000:
		y=(sales-25000)
		print("your commision is",(5000*.03)+(20000*.04)+(y*.05))
	elif sales>=100000:
		z=(sales-100000)
		print("your commision is",(5000*.03)+(20000*.04)+(75000*.05)+(z*.7))
	elif sales<=0:
		print("Head to HR")








