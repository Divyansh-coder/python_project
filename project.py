import csv
def write_file(student):
	with open("record.csv","a+",newline="") as file:
			content=csv.writer(file)
			if file.tell()==0:
				content.writerow(["Name","Age","Contact-no","E-mail"])
			content.writerow(student) 
if __name__=="__main__":
	choice=True
	student_count=1
	while choice:
		student=input("Enter the data of student #{} in format (First-name Last-name Age Contact_number E-mail): ".format(student_count)).split(" ")
		print("The student data entered:")
		print("1. Name: {} {}\n2. Age: {}\n3. Contact_number: {}\n4. E-mail: {}".format(student[0],student[1],student[2],student[3],student[4]))
		student[0]=student[0]+" "+student[1]
		del student[1]
		descision=input("Student data entered is correct? [Yes/No]: ").capitalize()
		if descision=="No":
			print("Please re-enter the values--")
		elif descision=="Yes":
			write_file(student)	
			choice_=input("Do you want to enter next student data [Yes/No]: ").capitalize()
			if choice_=="Yes":
				student_count+=1
			elif choice_=="No":
				choice=False
