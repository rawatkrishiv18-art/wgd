try:
    num = int(input("Enter your age : "))
    if num%2==0:
        print("your age is even")
    else:
        print("your age is odd")
    print("your age",num)
except ValueError as ex:
    print("Exception: ", ex)

except NameError as ex:
    print("The exception is ", ex)


