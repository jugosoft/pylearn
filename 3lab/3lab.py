def func(args):
    print(args)

def sum_arguments(args : list):
    result = 0
    for arg in args:
        result += arg
    return result

def is_smth_in_smwr(substr, str):
    return substr in str

def decorator_of_previous(args):
    return is_smth_in_smwr("abc", args)

def do_callback(function, *args):
    return function(args)

print(do_callback(sum_arguments, 256, 1337, 14, 22, 8, 0.8))

