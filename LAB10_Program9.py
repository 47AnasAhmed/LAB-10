print("Anas Ahmed (18B-116-CS) CS-A")
print("LAB10_Program9")
print("11/Jan/2019", "\n")

dict1 = {'Name': 'Jibran', 'Age': 12, 'Class': 'Sixth', 'DOB': '16 April 2006', 'School': 'The Seeds School'
, 'Friend1': 'Mohib', 'Friend2': 'Akbar', 'Friend3': 'Jazil'}

for x, y in dict1.items():
    print(x, y)
dict1.popitem()
print("After poping from the dictionary the remaining elements are:\n",dict1)



