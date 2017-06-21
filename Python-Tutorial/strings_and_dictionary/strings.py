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
