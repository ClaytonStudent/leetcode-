def cut(n):
    if n < 2 :
        return 0
    elif n == 2:
        return 1
    elif n == 3:
        return 2
    l = [0,1,2,3] # subproblem best solution 剪成长度为2，则最佳也是保留为2
    for i in range(4,n+1):
        max_num = 0
        for j in range(1,i//2+1):
            temp = l[j] * l[i-j]
            max_num = max(max_num,temp)
        l.append(max_num)
    return l[n] 

def cut_greedy(n):
    if n < 2:
        return 0
    if n == 2:
        return 1
    if n == 3:
        return 2
    times_of_3 = n // 3
    if n - times_of_3 *3 == 1:
        times_of_3 -= 1
    times_of_2 = (n-times_of_3*3) //2
    return pow(3,times_of_3)*pow(2,times_of_2)
print(cut(8))
print(cut_greedy(8))