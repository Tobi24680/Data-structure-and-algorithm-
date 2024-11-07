def binary_search(arr,target):
    left=0
    right=len(arr)-1
    
    while left <= right:
        mid=(left+right)//2
        if arr[mid]==target:
            return mid
        elif arr[mid]<target:
            left=mid+1
        else:
            right=mid-1
    return -1

if __name__=='__main__':
    input_list=input("enter sorted list of num(space seperated):").strip().split()
    arr=[int(num) for num in input_list]
    target=int(input('enter number to search:'))
    result=binary_search(arr,target)
    
    if result!=-1:
        print(f'element {target} is present at index {result}.')
    else:
        print('not found')

    
            