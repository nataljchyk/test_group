
import random
cn = input('Enter numbers of cities:')
cl = input('Enter numbers of line between cities:')
cstart = input('Enter the city to start:')
cend = input('Enter the city to end:')
s = ''
s1 = ''
k = int(cn)
k1 =int(cl)
n = 0
n1 = 0
while n < k1:
    s = s + str(random.randint(1, k))
    n += 1
print(s)

while n1 < k1:
    s1 = s1 + str(random.randint(1, k))
    n1 += 1
print(s1)

line = list(zip(s, s1))
print(line)

ss = list(zip(cstart, cend))
print(ss)
ss1 = list(zip(cend, cstart))
print(ss1)



# if ss in line:
#     print('Yes, there is a direct way', ss)
#     if ss1 in line:
#         print('Yes, there is a direct way', ss1)
# else:
#     print('No, there is not a direct way', ss, 'or', ss1)

# print(line.count(ss))
# print(line.count(ss1))

# if list(['1', '2']) in list([('1', '2'), ('2', '4'), ('4', '1'), ('1', '2'), ('4', '2'), ('4', '1'), ('1', '4'), ('4', '2'), ('2', '2')]):
#     print('great')
# else:
#     print('sorry')