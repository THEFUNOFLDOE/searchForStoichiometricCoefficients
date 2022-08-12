import re


def mol_divide(substance: str) -> list:
    split_mol = []
    brackets = re.search(r"""\(.*\)""", substance)  # check '()' brackets. Ba(OH)2 contain it.
    square_brackets = re.search(r"""\[.*]""", substance)  # check '[]' brackets. K4[Fe(CN)6] contain it.
    data = {'start': 0, 'end': 0, 'group_index': []}  # start - where brackets open, end - where close.
    # group_index - index of group of atom/ Like Ba(OH)2, 2 it`s group_index
    flag = False

    if square_brackets is not None:
        data['start'] = square_brackets.start()
        data['end'] = square_brackets.end()
        data['group_index'] = re.search(r"""^\d+""", substance[square_brackets.end():])
        flag = True

    elif brackets is not None:
        data['start'] = brackets.start()
        data['end'] = brackets.end()
        data['group_index'] = re.search(r"""^\d+""", substance[brackets.end():])
        flag = True

    else:
        # if any brackets have been found? just split rest

        index = 1

        while len(substance) > 0:
            if index < len(substance) and (substance[index].islower() or substance[index].isdigit()):
                index += 1

            else:
                split_mol.append(substance[:index])
                substance = substance[index:]
                index = 1

    if flag:
        start, end, group_index = data.values()  # unpack it
        if group_index is not None:
            split_mol.extend(
                mol_divide(substance[:start] + substance[end:][group_index.end():]))  # send rest of substance next
            raw_split_mol = mol_divide(substance[start + 1: end - 1])  # get part of substance in brackets
            # and send next it
            for index_, i in enumerate(raw_split_mol):
                index_ion = re.search(r"""\d+$""", i)  # get index of atom

                if index_ion is not None:
                    raw_split_mol[index_] = f'{i[:index_ion.start()]}' \
                                            f'{int(index_ion.group()) * int(group_index.group())}'
                    # multiply by group_index

                else:
                    raw_split_mol[index_] = i + group_index.group()  # or just add it to atom

            split_mol.extend(raw_split_mol)  # and add it to split_mol

        else:
            split_mol.extend(mol_divide(substance[:start] + substance[end:]))
            split_mol.extend(mol_divide(substance[start + 1: end - 1]))

    return split_mol
