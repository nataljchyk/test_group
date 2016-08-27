from string import ascii_lowercase
# a = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# b = 'XYZABCDEFGHIJKLMNOPQRSTUVW'
# dict1 = zip(a, b)
# print(dict(dict1))
a = ascii_lowercase
c = ''
key = int(input('Enter key: '))
s = input('Enter string:')
s1 = ''
c = a[-key:] + a[:-key]
print(a)
print(c)
dict1 = dict(zip(a, c))

for letter in s:
    s1 += dict1.get(letter, letter)
print(s1)

s2 = ''
dict2 = dict(zip(c, a))
for letter1 in s1:
    s2 += dict2.get(letter1, letter1)
print(s2)

# string
# translate()
# maketrans()
# do the same  task
