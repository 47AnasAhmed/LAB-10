print("Anas Ahmed (18B-116-CS) CS-A")
print("LAB10_Task1")
'''Write a function to design a personal phone directory of your parents and friends. You must add 12 members.
Then make a function to delete a member from a telephone directory. Print total number of members in your personal
phone directory.'''
print("11/Jan/2019", "\n")

phone_directory ={'M Adnan Shakil': '03332154686', 'Qudsia Hurmat': '03343037848', 'Umer Ahmed': '03343032019',
                  'Paternal G.Mother': '03598747978', 'Jawwad': '03372893478', 'Usman': '03332165674',
                  'Daniyal': '03342346785', 'Sarim': '03334564865', 'Hashim': '03118967988', 'Farhan': '0332765687658',
                  'Saad': '03327567456', 'Huzaifa': '03327954569'}
del phone_directory['M Adnan Shakil']
print(phone_directory)
print(len(phone_directory))