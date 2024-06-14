def f(money,interest,month):
    result=0
    for i in range(month):
        result+=money*((interest+100)/100)**(month-1)
    return result
print(f(1000000,1.74,3))