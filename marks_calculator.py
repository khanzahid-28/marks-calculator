m1=int(input("Subject 1 marks: "))
m2=int(input("Subject 2 marks: "))
m3=int(input("Subject 3 marks: "))
print(m1)
print(m2)
print(m3)
total=m1+m2+m3
print(total/3)
percentage=total/3
if percentage>=75:
	print("A")
elif percentage>=60:
	print("B")
elif percentage>=40:
	print("C")
else:
	print("Fail")
print(round(percentage,2))
