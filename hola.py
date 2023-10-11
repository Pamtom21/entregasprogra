def binary_search(arr, low, high, x):
 
    # Check base case
    if high >= low:
 
        mid = (high + low) // 2
 
        # If element is present at the middle itself
        if arr[mid] == x:
            return mid
 
        # If element is smaller than mid, then it can only
        # be present in left subarray
        elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x)
 
        # Else the element can only be present in right subarray
        else:
            return binary_search(arr, mid + 1, high, x)
 
    else:
        # Element is not present in the array
        return -1
 
# Test array
arr = [ 2, 3, 4, 10, 40 ]
x = 2
 
# Function call
#result = binary_search(arr, 0, len(arr)-1, x)
 
#if result != -1:
    #print("Element is present at index", str(result))
#else:
    #print("Element is not present in array")
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less = [x for x in arr[1:] if x <= pivot]
        greater = [x for x in arr[1:] if x > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)

# Ejemplo de uso
if __name__ == "__main__":
    arr = [12, 11, 13, 5, 6, 10]
    print("Arreglo no ordenado:", arr)

    sorted_arr = quick_sort(arr)

    print("Arreglo ordenado:", sorted_arr)