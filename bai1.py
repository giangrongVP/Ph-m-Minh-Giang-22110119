import math

# Hàm kiểm tra số nguyên tố
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

# Xử lý nhập liệu an toàn
while True:
    try:
        n = int(input("Nhập số nguyên dương n: "))
        if n < 0:
            print("Vui lòng nhập số nguyên dương!")
        else:
            break  # Thoát vòng lặp nếu nhập đúng
    except ValueError:
        print("Lỗi! Vui lòng nhập một số nguyên hợp lệ.")

# Kiểm tra và in kết quả
if is_prime(n):
    print(f"{n} là số nguyên tố.")
else:
    print(f"{n} không phải là số nguyên tố.")
