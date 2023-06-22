def swap_case(s : str)->str:
    answ = ''
    for i in range(len(s)):
        if s[i].islower():
            answ += s[i].upper()
        elif s[i].isupper():
            answ += s[i].lower()
        else:
            answ+=s[i]
    return answ

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
