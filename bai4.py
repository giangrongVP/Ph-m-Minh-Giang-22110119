def fibonacci(n):
    # Khởi tạo mảng để lưu trữ giá trị Fibonacci
    fib = [0] * (n + 1)
    
    # Gán giá trị cho các số Fibonacci đầu tiên
    fib[0] = 0
    if n > 0:
        fib[1] = 1
    
    # Tính toán các số Fibonacci tiếp theo
    for i in range(2, n + 1):
        fib[i] = fib[i - 1] + fib[i - 2]
    
    return fib[n]

# Nhập số n từ người dùng
n = int(input("Nhập số n: "))
result = fibonacci(n)
print(f"Số Fibonacci thứ {n} là: {result}")