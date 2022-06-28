from mol_divide import mol_divide
import re


def ion_counter(substance: str, index_mol: int) -> dict:
    ans = {}
    for i in mol_divide(substance):
        index = re.search(r"""\d+$""", i)

        if index is not None:
            i = i[:index.start()]
            index = int(index.group())

        else:
            index = 1

        if i in ans:
            ans[i] += index * index_mol

        else:
            ans[i] = index * index_mol

    return ans
