def f(s: str) -> int:
    if s == '':
        return 0
    elif s[-1] == 'a':
        return f(s[:-1])
    elif s[-1] == 'b':
        n = len(s) - 1
        return f(s[:-1]) + (2**n - 1) + 1
    else:
        n = len(s) - 1
        return f(s[:-1]) + 2* ((2**n - 1) + 1)


_ = input()
S = input()

print(f(S))
