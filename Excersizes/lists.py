# insertion sort for an array

arr = [3, 1, 8, 5, 2, 7, 10, 9, 4, 6] 
print(f'original arr {arr}')

for boundary_idx in range(len(arr)):
	for cur_idx in range(boundary_idx, 0, -1):
		if arr[cur_idx] < arr[cur_idx-1]: 
			arr[cur_idx], arr[cur_idx-1] = arr[cur_idx-1], arr[cur_idx]

print(f'sorted array {arr}')