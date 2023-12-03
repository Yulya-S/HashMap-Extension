class SpecialHashMap(dict):
    def __init__(self):
        self.iloc = iloc(self)
        self.ploc = ploc(self)


class iloc:
    def __init__(self, d):
        self.d = d

    def __getitem__(self, item):
        sort_names = sorted(self.d)
        if item > len(sort_names) - 1:
            raise ValueError("index out of range")
        else:
            return self.d[sort_names[item]]


class ploc:
    def __init__(self, d):
        self.d = d

    def parse_item(self, item):
        result = []
        if type(item) != str:
            raise ValueError("item is not str")
        if item == "":
            raise ValueError("Invalid key")
        item = item.split(',')
        for i in item:
            operation = ''
            number = ''
            for l in i:
                if l in ['>', '=', '<']:
                    operation += l
                elif l.isdigit() or l == '.':
                    number += l
                elif l != ' ':
                    raise ValueError("Invalid key")
            if operation != '' and number != '':
                result.append([operation, number])
            else:
                raise ValueError("Invalid key")
        return result

    def parse_keys(self):
        keys = []
        for i in self.d.keys():
            text = i.split(',')
            key = []
            for l in text:
                key.append('')
                for z in l:
                    if z.isdigit() or z == '.':
                       key[-1] += z
                    elif z not in ['(', ')', ' ']:
                        key = i
                        break
                if type(key) == str:
                    break
            keys.append(key)
        for i in range(len(keys)):
            if type(keys[i]) != str:
                for l in range(len(keys[i])):
                    keys[i][l] = float(keys[i][l])
        return keys

    def conditions(self, op, number, key):
        if op == '=':
            return key == number
        elif op == '>':
            return key > number
        elif op == '<':
            return key < number
        elif op == '>=':
            return key >= number
        elif op == '<=':
            return key <= number
        elif op == '<>':
            return key != number
        else:
            raise ValueError("Invalid conditions")

    def __getitem__(self, item):
        str_keys = list(self.d.keys())
        parse_keys = self.parse_keys()
        conditions = self.parse_item(item)

        result = {}
        for key in parse_keys:
            if type(key) != str:
                if len(key) == len(conditions):
                    correct = 0
                    for i in range(len(conditions)):
                        if self.conditions(conditions[i][0], float(conditions[i][1]), key[i]):
                            correct += 1
                    if correct == len(conditions):
                        result[str_keys[parse_keys.index(key)]] = self.d[str_keys[parse_keys.index(key)]]
        return result
