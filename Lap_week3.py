#!/usr/bin/env python
# coding: utf-8

# In[ ]:


password = input("Enter password: ")

if password == "admin123":
    print("Access Granted")
else:
    print("Access Denied")


# In[ ]:


age = int(input("Enter your age: "))

if age < 13:
    print("Child")
elif 13 <= age <= 19:
    print("Teen")
elif 20 <= age <= 59:
    print("Adult")
else:
    print("Senior")


# In[ ]:


number = int(input("Enter a number: "))

# Check if positive
if number > 0:
    print("Positive")
else:
    print("Not Positive")

# Check if between 10 and 50 (inclusive)
if 10 <= number <= 50:
    print("Number is between 10 and 50")
else:
    print("Number is NOT between 10 and 50")


# In[ ]:


color = input("Enter a color (red, yellow, green): ")

if color != "":
    match color:
        case "red":
            print("Stop")
        case "yellow":
            print("Wait")
        case "green":
            print("Go")
        case _:
            print("Invalid color")
else:
    print("Input cannot be empty")


# In[ ]:


print("Menu:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = input("Choose an option (1-4): ")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

match choice:
    case "1":
        result = num1 + num2
    case "2":
        result = num1 - num2
    case "3":
        result = num1 * num2
    case "4":
        if num2 != 0:
            result = num1 / num2
        else:
            result = "Cannot divide by zero"
    case _:
        result = "Invalid choice"

print("Result:", result)


# In[ ]:


score = float(input("Enter student score: "))

# Determine pass or fail
if score >= 50:
    status = "Passed"
else:
    status = "Failed"

# Assign grade
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
elif score >= 50:
    grade = "E"
else:
    grade = "F"

print("Status:", status)
print("Grade:", grade)

# Message using match
match grade:
    case "A":
        print("Excellent work!")
    case "B":
        print("Very good!")
    case "C":
        print("Good job!")
    case "D":
        print("You passed.")
    case "E":
        print("Barely passed.")
    case "F":
        print("Better luck next time.")

