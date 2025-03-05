# Function to find the non-repeated number in a list using sort and adjacent comparison
def find_non_repeated(arr):
    arr.sort()
    if len(arr) == 1 or arr[0] != arr[1]:
        return arr[0]
    if arr[-1] != arr[-2]:
        return arr[-1]
    for i in range(1, len(arr) - 1):
        if arr[i] != arr[i-1] and arr[i] != arr[i+1]:
            return arr[i]
    return None
arr = list(map(int, input("Enter the list of numbers separated by spaces: ").split()))

result = find_non_repeated(arr)
if result is not None:
    print(f"The non-repeated number in the list is: {result}")
else:
    print("No non-repeated number found in the list.")

