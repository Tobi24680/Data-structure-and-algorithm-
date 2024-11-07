def selection_sort(arr):
    n=len(arr)
    for i in range(n-1):
        min_index=i
        for j in range(i+1,n):
            if arr[j]<arr[min_index]:
                min_index=j
        if min_index!=i:
            arr[i],arr[min_index]=arr[min_index],arr[i]
            
def input1():
    input_str=input('enter a num seperated by space:')
    try:
        arr=list(map(int,input_str.split()))
    except ValueError:
        print("error")
        return None
    return arr

def main():
    arr=input1()
    if arr:
        print('original array:',arr)
        selection_sort(arr)
        print("sorted array:",arr)
if __name__=="__main__":
    main()

    