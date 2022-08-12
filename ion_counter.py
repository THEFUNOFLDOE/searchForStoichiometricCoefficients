from mol_divide import mol_divide
import re


# transform substance like 'H2O' into {'H': 2, 'O': 1}
def ion_counter(substance: str) -> dict:
    ans = {}
    for i in mol_divide(substance):
        index = re.search(r"""\d+$""", i)  # try to find index of ion or atom

        if index is not None:
            i = i[:index.start()]
            index = int(index.group())  # take it

        else:
            index = 1  # or 1

        if i not in ans:
            ans[i] = index

        ans[i] += index  # if substance like CH3OH - Methyl alcohol, should plus it, not add

    return ans
