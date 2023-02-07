import random

mylist1 = list(range(1,16))
mylist2 = list(range(16,30))
mylist3 = list(range(30,45))
mylist4 = list(range(45,60))
mylist5 = list(range(60,75))

random.shuffle(mylist1)
random.shuffle(mylist2)
random.shuffle(mylist3)
random.shuffle(mylist4)
random.shuffle(mylist5)

x = random.randint(1,75)
count = 0
summ1 = 0
summ2 = 0
summ3 = 0
summ4 = 0
summ5 = 0
summ6 = 0
summ7 = 0
print(summ1)
print(summ2)
print(summ3)
print(summ4)
print(summ5)
print(summ6)
print(summ7)

# for _ in mylist1:
    # for _ in mylist2:
        # for _ in mylist3:
            # for _ in mylist4:
                # for _ in mylist5:

if x == mylist1[0] or x == mylist2[0] or x == mylist3[0] or x == mylist4[0] or x == mylist5[0]:
                        summ1 += 1
                        count += 1
                        print(summ1,count)
elif x == mylist1[1] or x == mylist2[1] or x == mylist3[1] or x == mylist4[1] or x == mylist5[1]:
                        summ2 += 1
                        count += 1
                        print(summ2,count)
elif x == mylist1[2] or x == mylist2[2] or x == mylist3[2] or x == mylist4[2] or x == mylist5[2]:
                        summ3 += 1
                        count += 1
                        print(summ3,count)
elif x == mylist1[3] or x == mylist2[3] or x == mylist3[3] or x == mylist4[3] or x == mylist5[3]:
                        summ4 += 1
                        count += 1
                        print(summ4,count)
elif x == mylist1[4] or x == mylist2[4] or x == mylist3[4] or x == mylist4[4] or x == mylist5[4]:
                        summ5 += 1
                        count += 1
                        print(summ5,count)
elif x == mylist1[0] or x == mylist2[1] or x == mylist3[2] or x == mylist4[3] or x == mylist5[4]:
                        summ6 += 1
                        count += 1
                        print(summ6,count)
elif x == mylist1[4] or x == mylist2[3] or x == mylist3[2] or x == mylist4[1] or x == mylist5[0]:
                        summ7 += 1
                        count += 1
                        print(summ7,count)
print(f'Number drawn:{x}')
print(f'Total balls drawn:{count}')
print('B',mylist1[:5])
print('I',mylist2[:5])
print('N',mylist3[:5])
print('G',mylist4[:5])
print('O',mylist5[:5])

else:
            summ1 == 5 or summ2 == 5 or summ3 == 5 or summ4 == 5 or summ5 == 5 or summ6 == 5 or summ7 ==5
        print('bingo')


# x = random.randint(1,75)

# for i in mylist1,mylist2,mylist3,mylist4,mylist5:
#     if x in mylist1 or x in mylist2 or x in mylist3 or x in mylist4 or x in mylist5:
#         x == '#'
#         count += 1
#     else:
#         count += 1
#         pass
    

