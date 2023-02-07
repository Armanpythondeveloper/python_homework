#1.Write a Python program to sort a dictionary by value.
# mydict = {
#     'name' : 'mersedec',
#     'age' : '2020',
#     'color' : 'black',
# }
# a = sorted(mydict,key = mydict.get)
# print(a)


#2. Write a Python program to add a key to a dictionary.

# mydict = {
#     'name' : 'mersedec',
#     'age' : '2020',
#     'color' : 'black',
# }
# mydict['mator'] = ['350']
# print(mydict)

# 3. Write a Python program to check whether a given key already exists in a dictionary.

# mydict = {
#     'name' : 'mersedec',
#     'age' : '2020',
#     'color' : 'black',
# }

# keyy = 'name'
# for i in mydict:
#     if keyy in mydict:
#         print('arden ka ed anuny')
#         break
#     else:
#         print('chka ed anuny')
#         break

# 4.Write a Python program to merge two 
# Python dictionaries.
# dict1 = {'a': 50, 'b': 700}
# dict2 = {'c': 400, 'd': 600}
# dict1.update(dict2)
# print(dict1)
# output: {'a': 50, 'b': 700, 'c': 400, 'd': 600}

# 5. Write a Python program to multiply all the 
# values in a dictionary.
# For example:
# mydict = {'a':1,'b':2,'c':12} 
# res = 1
# for i in mydict:
#     res *= mydict[i]
# print(res)

# 6. Create a Python program to find the highest 
# 3 values in a dictionary.
# mydict = {'D': 56, 'E': 12, 'F': 69, 'C': 45, 'B': 23, 'A': 67}
# dict1 = {}
# a = sorted(mydict,key = mydict.get,reverse=True)[:3]
# myvalue = sorted(mydict.values(),reverse=True)[:3]
# for i , j in zip(a,myvalue):
#     dict1.setdefault(i,j)
# print(dict1)

# output: {'F': 69, 'A': 67, 'D': 56}

#-------------------------------------------22222222--------------------------
# mydict = {
#     'KAREN':8,
#     'ARTAK':9,
#     'VAHRAM':7,
#     'ANI':10,
#     'NARE':9,
# }
# count = 0
# sum = 0
# for _ in mydict:
#     x = mydict.values()
#     for i in x:
#         sum += i
#         count += 1
#         average = sum / count
# print(average)
    
# 3. GOOd And bAd sTudenT
# # Create a python program which will sayyou who they are good and bad students.

# mydict = {
#     'KAREN':4,
#     'ARTAK':9,
#     'VAHRAM':3,
#     'ANI':10,
#     'NARE':6,
#     'VAHE':7
# }
# # print(mydict.keys())
# x = mydict.values()
# for i in x:
#     if i >= 8:

#         print(f'{i}good')
#     else:
#         print('bad')

# 4. GOOd sTudenTs
# Create a python program which will saywho have 5 or great rating in your Students.

# mydict = {
#     'KAREN':4,
#     'ARTAK':9,
#     'VAHRAM':3,
#     'ANI':10,
#     'NARE':6,
#     'VAHE':7
# }
# dict1 = {}
# a = sorted(mydict,key = mydict.get,reverse=True)[:5]
# myvalue = sorted(mydict.values(),reverse=True)[:5]
# print(a,myvalue)

# for i , j in zip(a,myvalue):
#     dict1.setdefault(i,j)
# print(dict1)

# 6. nAme
# Create a python program which will sayif your dictionary have this name print name and rating.


# mydict = {
#     'KAREN':4,
#     'ARTAK':9,
#     'VAHRAM':3,
#     'ANI':10,
#     'NARE':6,
#     'VAHE':7
# }

# name = input('enter name: ')
# if name in mydict:
#     print(name,mydict[name])
# else:
#     print('chka')

# 7.New_dicT
# Create a new dictionary:For example...
# s = {'a':2,'b':5,'c':8,'a':4,'e':11}

# s['a'] += 2
# # {“a”:6,”b”:5,”c”:8,”e”:11}
# print(s)

#---------------------------888888888888888888888-------------------------
# word = 'excersise'
# mydict = {}
# for i in word:
#     if i in mydict:
#         mydict[i] += 1
#     else:
#         mydict[i] = 1
# print(mydict)
#-------------------------------9999999999999999-----------------------------------
# old_list = [{'key1':'value1'},{},{},{'key1':'value1'},{'key2':'value2'}] 
# new_list = []
# for i in old_list:
#     if old_list.count(i) == 2:
#         old_list.remove(i) 
#         new_list += str(i).split()
#     else:
#         new_list.append(i)
#         print(new_list)

#-------------------------------------------------------------------------------


# import time
# name = input('Enter Your name: ')
# print(f'Hello {name} welcome :)')
# start = input('Start Game?\n\tYes/No====>').title()
# if start == 'Yes':
#     print(3)
#     time.sleep(1)
#     print(2)
#     time.sleep(1)
#     print(1)
#     time.sleep(1)
#     print('-------------------------------------Start game ---------------------------------')
# else:
#     print('Game over')
# print('Erb e sksvel arajin hamashxarhayin paterazmmy?')


#148 greeeeeeel,#138,#139

# python3@
