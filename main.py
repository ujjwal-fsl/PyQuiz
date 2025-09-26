import csv
import ast
import operator

filename = "data.csv"
leader = "leaderboard.csv"

def stud_data():
	aid = input("Enter Student's ID:").strip()
	with open(leader, 'r') as file:
		content = csv.reader(file)
		temp=[]
		for row in content:
			if row[0] == aid:
				print(f"Student's ID: {row[0]}"
					  f"\nName: {row[1]}"
					  f"\nScore: {row[2]}")
				temp.append(row[0])
		if aid not in temp:
			print("Student Not Found.")

def leaderboard():
	print("\nLEADERBOARD!")
	print("“Champions aren’t born, they’re made on the leaderboard.”\n")
	with open(leader, 'r') as file:
		content = csv.reader(file)
		lb = sorted(content, key=operator.itemgetter(2),reverse=True)
		max = ""
		for i in lb:
			if len(max) < len(i[1]):
				temp = i[1]
				max = i[1]
		m = len(max)
		asp = " " * m
		print(f"ID Name{asp}Score")
		for i in lb:
			space = " " * (m - len(i[1]) + 4)
			print(f"{i[0]}  {i[1]}{space}{i[2]}")

def quiz():
	id = input("Enter Student ID:").upper().strip()
	name = input("Enter your name: ")
	print(f"ALL THE BEST {name}!\n")

	OPcode = ["A", "B", "C", "D"]
	score = 0

	with open(filename, 'r') as file:
		content = csv.reader(file)
		q = 1
		for i in content:
			Q = i[0]
			O = i[1]
			A = i[2]
			options_list = ast.literal_eval(O)
			O = set(options_list)

			print(f"{q}. {Q}")
			o = 0
			op = {}
			for opt in O:
				op[OPcode[o]] = opt
				print(f"{OPcode[o]}. {opt}")
				o += 1
			while True:
				answer = input("Enter your option:").upper()
				if answer in OPcode:
					if op[answer] == A:
						score += 1
						print("CORRECT!")
						break
					else:
						print("WRONG!")
						print(f"The correct answer is {A}.")
						break
				else:
					print("Invalid Option.")

			print()
			q += 1
		print(f"You scored {score} out of {q - 1}.")
		temp = [id, name, score]
		with open(leader, "a", newline='') as file:
			writer = csv.writer(file)
			writer.writerow(temp)

print("\nWELCOME TO THE QUIZ!")

entry = input("Enter S for STUDENT or A for ADMIN login :").upper().strip()
if entry == 'A':
	id = input("Enter Admin ID:").strip()
	pas = input("Enter Password:").strip()
	if id=="ADMIN" and pas=="admin":
		print("WELCOME ADMIN!")
		ac = input("1 - Question Input Portal\n2 - Student Data Portal\n3 - Leaderboard\nEnter Portal Code: ").strip()
		if ac == "1":
			import Add_Questions
		elif ac == "2":
			print("Welcome to the Student Data Portal!")
			while True:
				stud_data()
				ch = input("Want another Student's data? (Y/N)").upper().strip()
				if ch == "N":
					print("Thank You!")
					break
				elif ch == "Y":
					pass
				else:
					print("Invalid Input.")
					break
		elif ac == "3":
			leaderboard()
	else:
		print("Access Denied\nINCORRECT CREDENTIALS!")

elif entry == 'S':
	sc = input("1 - Participate in Quiz\n2 - Check Student Data\n3 - Leaderboard\nEnter Option: ").strip()
	if sc == "1":
		quiz()
	elif sc == "2":
		stud_data()
	elif sc == "3":
		leaderboard()

else:
	print("INVALID CHOICE!")