"""def main(x):
    dict31 = {'SMALI': 0, 'VCL': 1}
    dict32 = {'SMALI': 1, 'VCL': 3}
    dict33 = {1991: 4, 1966: 5, 1965: 6}
    dict34 = {1991: 7, 1966: 8, 1965: 9}

    dict21 = {'LLVM': dict31[x[1]], 'TOML': dict32[x[1]], 'XC': dict33[x[3]]}
    dict22 = {'SMALI': dict34[x[3]], 'VCL': 10}

    dict1 = {'GOSU': dict21[x[2]], 'LATTE': dict22[x[1]]}

    return dict1[x[0]]


print(main(['LATTE', 'SMALI', 'XC', 1965]))"""


def main(x):
    dict31 = {2020: 0, 2005: 1, 1976: 2}
    dict32 = {2020: 5, 2005: 6, 1976: 7}
    dict33 = {2020: 8, 2005: 9, 1976: 10}

    dict21 = {1965: dict31[x[2]], 1985: 3, 1994: 4}
    dict22 = {1965: dict32[x[2]], 1985: dict33[x[2]], 1994: 11}

    dict1 = {2018: dict21[x[3]], 1966: dict22[x[3]]}

    return dict1[x[1]]


print(main(['TCL', 1966, 2005, 1985]))





