print("Anas Ahmed (18B-116-CS) CS-A")
print("LAB10_Task1")
''' Design a dictionary of your family. Once you get the printout, update family dictionary
 with your grandparents (maternal and paternal).'''
print("11/Jan/2019", "\n")

family = {'Father': 'M Adnan Shakil', 'Mother': 'Qudsia Hurmat', 'Brother1': 'Umer Ahmed', 'Brother2': 'Zaid Ahmed',
          'Sister': 'Mina Ahmed'}
print(family)
family['Maternal G.Father'] = 'Arif Ali'
family['Maternal G.Mother'] = 'Shahida'
family['Paternal G.Father'] = 'Shakil Ahmed'
family['Paternal G.Mother'] = 'Anjum Shakil'
for x, y in family.items():
    print(x,':', y)


    