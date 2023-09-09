from img1 import draw1
from img2 import draw2
from square import draw_square

def main():
	
	print("Choose an option:")
	print("1. First Image a Square Spiral")
	print("2. Cool Colorful Spiral")
	print("3. White Square")
	
	# Get user input
	choice = input("Enter the number of your choice: ")
	
	# Check the user's choice and perform actions accordingly
	if choice == "1":
		# print("You chose Option 1")
		draw1()
	elif choice == "2":
		draw2()
	elif choice == "3":
		draw_square()
	else:
		print("Invalid choice. Please select a valid option (1, 2, or 3).")
main()
