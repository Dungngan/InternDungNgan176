def twoSumNaive(num_arr, pair_sum):
  # search first element in the array
  for i in range(len(num_arr) - 1):
    # search other element in the array
    for j in range(i + 1, len(num_arr)):
      # if these two elemets sum to pair_sum, print the pair
      if num_arr[i] + num_arr[j] == pair_sum:
        print("Pair with sum", pair_sum,"is: (", num_arr[i],",",num_arr[j],")")

      

# Driver Code
num_arr = [2, 7, 11, 15]
pair_sum = 7

# Function call inside print
twoSumNaive(num_arr, pair_sum) 