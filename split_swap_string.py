def split_half(s):
    if len(s) % 2 != 0:
        s1 = (len(s)//2) + 1
        print(s[s1:] + s[:s1])

Result = split_half("bbbbbcaaaaa")
