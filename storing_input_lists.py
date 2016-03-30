## Placing 5 user inputs into a list

numbers = []
count = 0

while count < 6:
    num = int(input("Enter a value"))
    count += 1
    numbers.append(num)

print(numbers)
print("The first number is", numbers[0])
print("The last number is", numbers[-1])
print("The smallest number is", min(numbers))
print("The largest number is", max(numbers))
print("The average number is", sum(numbers)/len(numbers))