def power(base, exp):
    if exp == 0:
        return 1
    else:
        ans = base * power(base, exp-1)
        return ans

print(power(2,4))
