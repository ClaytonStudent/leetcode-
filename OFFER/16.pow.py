def pow(base,exponent):
    if exponent == 0:
        return 1
    if base == 0:
        return 0
    ans = 1
    for _ in range(abs(exponent)):
        ans *= base
    if exponent < 0:
        ans = 1 / ans
    return ans



def power(base,exponent):
    if equal_zero(base) and exponent <0:
        raise ZeroDivisionError
    result = pow_(base,abs(exponent))
    if exponent < 0:
        return 1.0 / result
    else:
        return result

def equal_zero(num):   # 浮点数相等不能直接用==
    if abs(num-0.0) < 0.0000001:
        return True

def pow_(base,exponent):
    if exponent == 0:
        return 1
    if exponent == 1:
        return base
    result = pow_(base,exponent >> 1) # 用右移替代除以2
    result *= result
    if exponent & 0x1 == 1:  # 用位与替代除余
        result *= base
    return result

#print(pow(2,2))
print(power(2,7))