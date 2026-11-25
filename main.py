name = input("Nhap ten san pham: ")
price = int(input("Nhap don gia: "))
quantity = int(input("Nhap so luong: "))
tong_tien = price * quantity
print("\n--- HÓA ĐƠN ---")
print(f"Tên sản phẩm: {name}")
print(f"Đơn giá: {price}")
print(f"Số lượng: {quantity}")
print(f"Tổng tiền: {tong_tien}")