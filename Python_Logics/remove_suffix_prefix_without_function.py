string = 'lokendra'
prefix_remove = 'lo'

if string[:len(prefix_remove)] == prefix_remove:
    result = string[len(prefix_remove):]

else:
    result = string

print(result)

string = 'lokendra'
suffix_remove = 'dra'

if string[-len(suffix_remove):] == suffix_remove:
    result = string[0 : -len(suffix_remove)]

else:
    result = string

print(result)