# Array slicing
family = ['mom', 'dad', 'bro', 'sis', 'dog', 'wife', 'child1', 'child2']

print(family[3:])  # 3 to end of the list
print(family[:3])  # start of the list till 3 (excluded)
print(family[1:2])  # print from index 1 till 2 (excluded)
print(family[:])  # print the whole thing
print(family[1:7:2])  # print from index 1 to 7 (excluded) with jumps of two
print(family[-7:-1:1])  # print from 7 (excluded) to 1 with jumps of 1 (prints in correct sequence)
print(family[7:1:-1])  # print from 7(included) to 1 (excluded) backwards with jumps of 1 in reverse
print(family[::-2])  # print the whole list backwards with jumps of 2
