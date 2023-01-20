#Code For Part 1#
"""
a=input("How many seconds from 0-86,399 would you like to see?")
a=int(a)
#Taking the remainder of seconds and switching it to minutes
b=a/60
seconds=a%60
b=int(b)
minutes=b%60
#Making minutes into hours
c=b/60
c=int(c)
hours=c
print(a,"seconds is",hours,"hour",minutes,"minutes",seconds,"seconds")
"""
"""
#Code for Part 2#
population=input("What is the US population?:")
days=input("How many days from Dec 31st,2021?:")
hours=input("How many hours?:")
minutes=input("How many minutes?:")
seconds=input("How many seconds?:")
#Convert Days to Seconds
a=days
a=int(a)
a1=a*24*60*60
#Convert Hours to Seconds#
b=hours
b=int(b)
b1=b*60*60
#Convert Minutes to Seconds#
c=minutes
c=int(c)
c1=c*60
#Defining Seconds#
d1=seconds
d1=int(d1)
#Adding all the Seconds#
z=a1+b1+c1+d1
#Calculating Population#
births=z/7
deaths=z/13
immigrants=z/35
z2=births-deaths+immigrants
y=population
y=int(y)
z3=z2+y
z3=int(z3)
print("The population is around",z3,"people")
"""
"""
#Code for Part 3
a=input("How many second since the beginning of the year?:")
a=int(a)
#Taking the remainder of seconds and switching it to minutes
b=a/60
seconds=a%60
b=int(b)
minutes=b%60
#Making minutes into hours
c=b/60
c=int(c)
hours=c%24
#Making Hours into Days#
d=c/24
d=int(d)
days=d
#Calculating Population#
births=a/7
deaths=a/13
immigrants=a/35
z2=births-deaths+immigrants
population=334205119
y=population
y=int(y)
z3=z2+y
z3=int(z3)
print(days,"days",hours,"hours",minutes,"minutes",seconds,"seconds after the start of 2022, the total population was", z3)
"""

#Code for Part 4#
a=input("How many second since the beginning of the year?:")
a=int(a)
#Taking the remainder of seconds and switching it to minutes
b=a/60
seconds=a%60
b=int(b)
minutes=b%60
#Making minutes into hours
c=b/60
c=int(c)
hours=c%24
#Making Hours into Days#
d=c/24
d=int(d)
days=d
#Calculating Population#
births=a/7
deaths=a/13
immigrants=a/35
z2=births-deaths+immigrants
population=334205119
y=population
y=int(y)
z3=z2+y
z3=int(z3)
#Math for FlapJacks
f=(((z3+350)**2-12)/50)**(1/5)
f=int(f)
#Output
print(days,"days",hours,"hours",minutes,"minutes",seconds,"seconds after the start of 2022, the total population was", z3)
print("The average amount of flapjacks eaten is",f)


