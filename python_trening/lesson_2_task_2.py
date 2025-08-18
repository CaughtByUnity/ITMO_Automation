def string_length(s: str = '') -> int:
    return len(s)

def function(a: list, b: list) -> int:
    return max(len(a), len(b))

print(string_length('123'))
print(function([1, 2, 3], [4, 5, 6, 7, 8, 9, 10]))

def list_plus_element(x: list, y) -> list:
    x.append(y)
    return x

def list_sum(x: list) -> int:
    summa = sum(x)
    return summa

print(list_sum((1, 2, 3, 4)))
