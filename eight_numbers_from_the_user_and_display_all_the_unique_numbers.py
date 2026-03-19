'''Write a program to input eight numbers from the user and display all the unique 
numbers (once). '''


numbers = []
print("Enter 8 numbers:")

for i in range(8):
    num = int(input(f"Number {i+1}: "))
    numbers.append(num)

# Get unique numbers using set
unique_numbers = list(set(numbers)) 

print("\nOriginal numbers:", numbers)
print("Unique numbers:", unique_numbers)




