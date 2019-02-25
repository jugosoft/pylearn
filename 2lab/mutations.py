#1
print('example 1')
my_list = [[1, 2], ['a', 'b']]
my_tuple = ('foo', 'bar', )

new_list = my_list #list stays mutable
new_tuple = my_tuple #new_tuple is not connected with my_tuple

my_list.append([True, False]) #both list variables will get 
my_tuple += ('baz', ) #my_tuple will not change

print(my_list, new_list)
print(my_tuple, new_tuple)

del my_list
del my_tuple
del new_list
del new_tuple

import copy

#2
print('example 2:') 
var = {'list': [[1, 2], ['a', 'b']], 'tuple': ('foo', 'bar', )}
new_var = var.copy()
var.update({'str': 'string'})
var['list'].append([True, False])
var['tuple'] += ('baz', )

print(var)
print(new_var)

del var
del new_var


#3
print('example 3')
var = {'list': [[1, 2], ['a', 'b']], 'tuple': ('foo', 'bar', )}
new_var = copy.deepcopy(var)
var.update({'str': 'string'})
var['list'].append([True, False])
var['tuple'] += ('baz', )

print(var)
print(new_var)
