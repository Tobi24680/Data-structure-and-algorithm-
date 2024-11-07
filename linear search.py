def linear_search(arr,x):
    for i in range(len(arr)):
        if arr[i]==x:
            return i
    return -1

def print1():
    try:
        elements=input("enter elements of list separated by space:").strip().split()
        arr=[int(e)for e in elements]
        return arr
    except ValueError:
        print("Error:Enter integers only.")
        return print1()
def main():
    arr=print1()
    try:
     x=int(input("Enter the element to search for:"))
    except ValueError:
       print("Error:Please enter a valid integer")
       return

    result=linear_search(arr,x)
    
    if result!=-1:
        print("element",x,"found at index",result)
    else:
       print("element not found")

if __name__=="__main__":
   main()          