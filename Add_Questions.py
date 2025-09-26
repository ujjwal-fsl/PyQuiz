import csv

filename = "data.csv"

print("\nWELCOME to the Questions Input Panel!\n")

while True:
	Q = input("Enter the Question: ").strip()
	O = []
	ad = []
	for i in range(4):
		op = input(f"Enter option {i + 1}: ").strip()
		O.append(op)
	An = int(input("Enter the Correct Answer (option no.): "))

	if str(An) not in "1234":
		print("INVALID INPUT!")
		An = int(input("Enter the Correct Answer (option no.): "))

	A = O[An - 1]

	O = list(O)

	ad.append(Q)
	ad.append(O)
	ad.append(A)

	with open(filename, "a", newline='') as file:
		writer = csv.writer(file)
		writer.writerow(ad)

	c = input("Want to add more Questions? (Y/N)").upper().strip()
	if c == 'N':
		print("Thanks for adding the question(s)!")
		break
	elif c not in "YN":
		print("INVALID INPUT!")
		break