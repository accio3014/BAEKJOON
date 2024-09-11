T = int(input())

for _ in range(T) :
    change = [0, 0, 0, 0]
    C = int(input())

    if(C % 25 >= 0) :
        change[0] = C // 25
        C = C % 25
     
    if(C % 10 >= 0) :
        change[1] = C // 10
        C = C % 10
    
    if(C % 5 >= 0) :
        change[2] = C // 5
        C = C % 5
    
    change[3] = C

    for i in change :
        print(i, end=' ')
    print()