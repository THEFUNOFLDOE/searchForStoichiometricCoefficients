from ion_counter import ion_counter
from gauss import gauss
from find_fraction import find_fraction
from numpy import array, around
from fraction import Fraction


def equation(raw_eq: str) -> [str, dict]:
    split_equation = [j for i in raw_eq.split(' -> ') for j in i.split(' + ')]
    l_eq,  r_eq = map(lambda x: x.split(' + '), raw_eq.split(' -> '))
    matrix = {}
    for index, mol in enumerate(split_equation):
        for key, value in ion_counter(mol, 1).items():
            if key not in matrix:
                matrix[key] = {f'x{i}': Fraction(0) for i in range(1, len(split_equation) + 1)}

            matrix[key][f'x{index+1}'] = Fraction(value) if mol in l_eq else Fraction(-value)

    matrix = [[*value.values()] for value in matrix.values()]
    matrix = [[j for j in i] for i in gauss(matrix)]

    res = {f'x{j+1}': Fraction(1) for j in range(len(matrix[0]))}

    for i in matrix[::-1]:
        del_list = []
        data = {f'x{j+1}': i[j] for j in range(len(i))}

        for key, value in data.items():
            if value.num == 0:
                del_list.append(key)

        for g in del_list:
            del data[g]

        if len(data) == 0:
            continue

        key_item = [*data.keys()][0]
        del data[key_item]

        result_koef = Fraction(0)
        for x, val in data.items():
            result_koef += val*res[x]*-1
        res[key_item] = result_koef

    max_denom = max(map(lambda x: x.denom, res.values()))
    k_list = [int(i.num*max_denom/i.denom) for i in res.values()]

    k_dict = dict(zip(split_equation, k_list))
    l_part, r_part = [[f"{k_dict[key] if k_dict[key] not in [0, 1]  else ''}{key}" for key in part] for part in [l_eq, r_eq]]
    return f"""{' + '.join(l_part)} -> {' + '.join(r_part)}"""

