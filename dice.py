import random
choice="!"
while choice!='NO' and choice!='no' and choice!='No':
	rand=random.randint(1,6)
	print(rand)
	if(rand==6):
		print("Lucky person")
	print("Do you want to role the dice agin (yes/no)")
	choice=raw_input()


print("Thanx for using my python dice")	