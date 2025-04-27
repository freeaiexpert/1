# ------------------------------
# ✅ 1. Start
# ------------------------------

# ✅ 2. Get the number of elements from the user
N = int(input("Enter the number of elements: "))

# ✅ 3. Initialize an empty list
arr = []

# ✅ 4. Take input for each element manually
for i in range(N):
    val = int(input(f"Enter element {i+1}: "))
    arr.append(val)

print("\nOriginal array:", arr)

# ------------------------------
# ✅ 5. Perform Selection Sort
for i in range(N):
    # Assume the current index has the minimum value
    min_index = i

    # Find the actual smallest element in the rest of the array
    for j in range(i + 1, N):
        if arr[j] < arr[min_index]:
            min_index = j

    # Swap the smallest element with the current element
    arr[i], arr[min_index] = arr[min_index], arr[i]

# ------------------------------
# ✅ 6. Print the sorted array
print("Sorted array:", arr)

# ✅ 7. End
