sachin = 'hey there %s, how\'s your %s?'
verb = ('betty', 'foot')
print(sachin % verb)  # like C i.e. printf("%d", marks)

print(sachin.find('there'))

temp = ['1', '2', '3']
dash = '-'
print(dash.join(temp))

print(sachin.upper())
print(sachin.lower())
print(sachin.capitalize())

print(sachin.replace('your', 'my'))

# raw string (Ignores control characters)
print(r'C:\temp')

string = """"This is a simple lonnggg string which has spans across multiple lines, and consists of TABs and NEWLINE 
characters"""

print(string)

print(u'string')
