prev2 =0
prev1=1
print(prev2)
print(prev1)
for i in range(10):
    new_fibo= prev1+prev2
    print(new_fibo)
    prev2=prev1
    prev1=new_fibo
    
print(0)
print(1)
count=2
def fibonacci(prev1,prev2):
    global count
    if count <=19:
        new_fibo= prev1 +prev2
        print(new_fibo)
        prev2=prev1
        prev1=new_fibo
        count+=1
        fibonacci(prev1,prev2)
    else:
        return
fibonacci(1,0)

def F(n):
    if n<=1:
        return n
    else:
        return F(n-1)+F(n-2)
print(F(10))
