def unique_char(char):
    uniq_char = []
    for i in char:
        if i not in uniq_char:
            if char.count(i) == 1:
                print(i)
            else:
                uniq_char.append(i)
    return""
unique_char("google")