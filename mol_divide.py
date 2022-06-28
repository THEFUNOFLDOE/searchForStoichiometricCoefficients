import re


def mol_divide(substance: str) -> list:
    split_mol = []
    brackets = re.search(r"""\(.*\)""", substance)
    square_brackets = re.search(r"""\[.*]""", substance)
    data = {'start': 0, 'end': 0, 'index_group': [], 'main_group': None}
    flag = False

    if square_brackets is not None:
        data['start'] = square_brackets.start()
        data['end'] = square_brackets.end()
        data['index_group'] = re.search(r"""^\d+""", substance[square_brackets.end():])
        data['main_group'] = square_brackets
        flag = True

    elif brackets is not None:
        data['start'] = brackets.start()
        data['end'] = brackets.end()
        data['index_group'] = re.search(r"""^\d+""", substance[brackets.end():])
        data['main_group'] = brackets
        flag = True

    else:
        index = 1

        while len(substance) > 0:
            if index < len(substance) and (substance[index].islower() or substance[index].isdigit()):
                index += 1

            else:
                split_mol.append(substance[:index])
                substance = substance[index:]
                index = 1

    if flag:
        start, end, index_group, main_group = data.values()

        if index_group is not None:
            split_mol.extend(mol_divide(substance[:main_group.start()] + substance[main_group.end():][index_group.end():]))
            raw_split_mol = mol_divide(substance[start + 1: end-1])

            for index_, i in enumerate(raw_split_mol):
                index_ion = re.search(r"""\d+$""", i)

                if index_ion is not None:
                    raw_split_mol[index_] = f'{i[:index_ion.start()]}{int(index_ion.group()) * int(index_group.group())}'

                else:
                    raw_split_mol[index_] = i+index_group.group()
            split_mol.extend(raw_split_mol)

        else:
            split_mol.extend(mol_divide(substance[:main_group.start()] + substance[main_group.end():]))
            split_mol.extend(mol_divide(substance[start + 1: end - 1]))

    return split_mol
