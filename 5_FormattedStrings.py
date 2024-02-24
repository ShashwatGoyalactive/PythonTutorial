# formatted strings are used for creating dynamic strings

first = 'Shashwat'
last = 'Goyal'

# two ways of creating formatted string
# 1.Cooncatenation operator

messaege = first + ' [' + last + '] is a coder '
print(messaege)

# 2. using 'f' as perfix and for strings and inserting other strings inside curly braces

msg =  f'{first} [{last}] is a coder'
print(msg)