# text = input('Enter pangram:')
# set_text = set(text.lower())
# alpha = ('abcdefghijklmnopqrstuvwxyz')
# if set_text.issuperset(alpha):
#     print('This is truly pangram')
# else:
#     print('This is not pangram')

alphabet = 'abcdefghijklmnopqrstuvwxyz'
def check(text):
    return set(text.lower()).issuperset(set(alphabet))
#  function issupperset - return always true/false
