# Function to process the list and calculate the result
def process_list(arr):
    even_sum = sum(num for num in arr if num % 2 == 0)
    odd_sum = sum(num for num in arr if num % 2 != 0)
    result = even_sum * odd_sum
    return result

# Sample input list
arr =list(map(int,input("enter the list:").split()))

# Calculate and display the result
result = process_list(arr)
print(f"The result of multiplying the sum of even terms and odd terms is: {result}")
