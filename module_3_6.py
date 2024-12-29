data_structure = [[1, 2, 3], {'a': 4, 'b': 5},
                      (6, {'cube': 7, 'drum': 8}),
                      "Hello", ((),[{(2, 'Urban', ('Urban2', 35))}])]
def calculate_structure_sum (*args):
    sum_len_2 = 0
    sum_0 = 0
    sum_1 = []
    for i in data_structure:
        if type (i) == dict:
            for x,y in i.items():
                if type(y) == int:
                    sum_1.append(y)
                else:
                    continue
        if type (i) == tuple:
            for z in i:
                if type (z) == dict:
                    for a,b in z.items():
                        if type(a) == int:
                            sum_1.append(a)
                        elif type(b) == int:
                            sum_1.append(b)
                        else:
                            continue
                if type (z) == list:
                    for m in z:
                        if type (m) == set:
                            for s in m:
                                if type(s) == tuple:
                                    for d in s:
                                        if type(d) == int:
                                            sum_1.append(d)
                                        elif type(d) == tuple:
                                            for u in d:
                                                if type(u) == int:
                                                    sum_1.append(u)

                        else:
                            continue
        for j in i:
            if type(j) == int:
                sum_1.append(j)
    for o in sum_1:
        if type(o) == int:
            sum_0 += o
    return sum_0
print(calculate_structure_sum(data_structure))