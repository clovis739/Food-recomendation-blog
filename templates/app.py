def print_numbers():
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("UBCOT")
        elif i % 3 == 0:
            print("UB")
        elif i % 5 == 0:
            print("COT")
        else:
            print(i)

# Call the function
print_numbers()



