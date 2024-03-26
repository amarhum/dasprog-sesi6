for i in range(5):
    for j in range(i,5):
        if(i+j)%2==0:
            print("S",end=' ')
        else:
            print("O",end=' ')
    print()