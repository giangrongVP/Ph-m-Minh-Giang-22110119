# Hàm sắp xếp Bubble Sort
def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):  # Lặp qua mảng n-1 lần
        swapped = False  # Biến kiểm tra có hoán đổi không
        for j in range(n - 1 - i):  # Giảm số lần duyệt vì phần cuối đã được sắp
            if arr[j] > arr[j + 1]:  # Nếu phần tử trước lớn hơn phần tử sau, hoán đổi
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:  # Nếu không có hoán đổi, mảng đã sắp xếp xong
            break

# Nhập mảng từ người dùng
arr = list(map(int, input("Nhập các số nguyên, cách nhau bởi dấu cách: ").split()))

# Sắp xếp mảng
bubble_sort(arr)

# In kết quả
print("Mảng sau khi sắp xếp:", arr)
