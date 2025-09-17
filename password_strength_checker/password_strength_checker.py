password = input("Enter your password: ")

if len(password) < 6:
    print("Weak: Password is too short.")
elif password.isalpha():
    print("Weak: Use numbers or symbols too.")
elif password.isdigit():
    print("Weak: Use letters and symbols too.")
elif password.isalnum():
    print("Medium: Add some symbols for better security.")
else:
    print("Strong: Good job!")
    
