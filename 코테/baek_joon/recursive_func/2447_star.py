def star(a):
    if a==3:
        return 0
    cnt=0
    for i in range(a//3):
        for j in range(a//3):
            if i%3 ==1 and j%3==1:
                print(" ",end='')
                continue
            print("*",end='')
        print()
      



star(27)
'''
*********
* ** ** *
*********
***   ***
* *   * *
***   ***
*********
* ** ** *
*********
'''