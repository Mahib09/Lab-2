def greaterthan(mynumbers):
    greaterlist=[]
    for num in mynumbers:
        if num > 5:
            greaterlist.append(num)
    print(greaterlist)
mynumbers = [1, 2, 3,4,5,6,7,8,9,10]
print("All elements in the list:")
print(mynumbers)
print("\nElements in the list greater than 12:")
greaterthan(mynumbers)

