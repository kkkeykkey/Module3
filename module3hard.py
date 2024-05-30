data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])]


def calculate_structure_sum(data_structure):
    result = 0
    for i in data_structure:
        i_type = type(i)
        if i_type == int:
            result += i
        elif i_type == str:
            result += len(i)
        elif i_type == dict:
            result += calculate_structure_sum(i.keys())
            result += calculate_structure_sum(i.values())
        else:
            result += calculate_structure_sum(i)
    return result


result = calculate_structure_sum(data_structure)
print(result)
