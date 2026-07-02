datam = [4,8,10,12]
for item in datam:
    if item % 2 == 0:
        datam.append(item + 2)
        break
print("No good item found")