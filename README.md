# Order Calculator

A simple Python program that calculates the total price of an order.

## What it does

1. Asks for the product name, unit price and quantity.
2. Calculates the total price (price x quantity).
3. Prints a simple invoice.

## How to run

On Windows, open a terminal in this folder and run:

```
python -m venv .venv
.venv\Scripts\Activate.ps1
python main.py
```

## Example

```
Nhap ten san pham: cocacola
Nhap don gia: 50000
Nhap so luong: 3

--- HÓA ĐƠN ---
Tên sản phẩm: cocacola
Đơn giá: 50000
Số lượng: 3
Tổng tiền: 150000
```

## Known limitations

- Price and quantity must be whole numbers. Letters (for example `abc`) crash the program with a ValueError.
- A negative quantity gives a negative total, because there is no input check yet.