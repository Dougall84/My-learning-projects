largest = None
smallest = None

while True:
    numinput = input("Enter a number: ")

# check for exit command and invaild inputs
    if numinput == "done":
        break
    try:
        num = int(numinput)    
    except:
        print('Invalid input')
        continue
    
# compare smallest to input and store
    if smallest is None:
        smallest = num
        
    elif num < smallest :
        smallest = num

# compare largest to input and store
    if largest is None :
        largest = num

    elif num > largest :
        largest = num
        
print("Maximum", largest)
print("Minimum", smallest)
