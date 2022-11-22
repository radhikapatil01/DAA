# Python program to display the Fibonacci sequence

def recur_fibo(n):
   if n <= 1:
       return n
   else:
       return(recur_fibo(n-1) + recur_fibo(n-2))

def Fib(n):
    a,b = 0,1
    for i in range(n):
        a,b = b, a+b
    return a


def main():
    while True:
        nterms = 10
        print("Select your choice-")
        print("1. Using recursive function")
        print("2. Using non-recursive function")
        print("3. Exit")
        ch=int(input("Enter your choice: "))
        if(ch==1):
            # check if the number of terms is valid
            if nterms <= 0:
                print("Plese enter a positive integer")
            else:
                print("Fibonacci sequence using recursive function:")
                for i in range(nterms):
                    print(recur_fibo(i))
        elif(ch==2):
            if nterms <= 0:
                print("Plese enter a positive integer")
            else:
                print("Fibonacci sequence using non-recursive function:")
                for i in range(nterms):
                    print(Fib(i))
        else:
            print("Program exited successfully!")
            break
        
main()
quit()