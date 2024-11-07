def merge_sort(arr):
    if len(arr)>1:
        mid=len(arr)//2
        left=arr[:mid]
        right=arr[mid:]
        merge_sort(left)
        merge_sort(right)
        i=j=k=0
        while i<len(left) and i<len(right):
            if left[i]<right[j]:
                arr[k]=left[i]
                i+=1
            else:
                arr[k]=right[j]
                j+=1
            k+=1
        while i<len(left):            
            arr[k]=left[i]
            i+=1
            k+=1
        while j<len(right):
            arr[k]=right[j]
            j+=1
            k+=1
        return arr
if __name__=="__main__":
    input_list=input("enter a num").strip().split()
    arr=[int(num) for num in input_list]
    print("original array",arr)
    merge_sort(arr)
    print("sorted",arr)
    
                      
                