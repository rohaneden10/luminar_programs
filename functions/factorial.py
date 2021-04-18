def factorial():
    num=int(input("enter a no"))
    factorial=1
    for i in range(1,(num+1)):
        factorial=factorial*i
    print(factorial)
factorial()