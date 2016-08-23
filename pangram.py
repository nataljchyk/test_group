# text = input('Enter pangram:')
# set_text = set(text.lower())
# alpha = ('abcdefghijklmnopqrstuvwxyz')
# if set_text.issuperset(alpha):
#     print('This is truly pangram')
# else:
#     print('This is not pangram')

# Coopyright unknown 2016
from string import ascii_lowercase as az


# alphabet = 'abcdefghijklmnopqrstuvwxyz'
def check(text):
    return set(text.lower()).issuperset(set(az))
#  function issupperset - return always true/false

print(check('abc'))
