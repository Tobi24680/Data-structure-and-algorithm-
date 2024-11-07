def buble_sort(arr):
    n=len(arr)
    for i in range(n):
        swapped=False
        for j in range(0,n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
                swapped=True   
        if not swapped:
            break
    return arr
if __name__=='__main__':
    input_list=input('enter a list of number(space seperated)').strip().split()
    arr=[int(num) for num in input_list]
    print('original array:',arr)
    buble_sort(arr)
    print('sorted array:',arr)
      