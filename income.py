import tkinter as tk
from tkinter import messagebox

def calculate():
    try:
        # 获取用户输入的值
        buy_price = float(entry_buy_price.get())
        sell_price = float(entry_sell_price.get())

        # 如果杠杆为空，则设置为 1
        leverage = float(entry_leverage.get()) if entry_leverage.get() else 1
        usdt_amount = float(entry_usdt_amount.get())

        # 如果杠杆为空，则在界面上显示 1
        if not entry_leverage.get():
            entry_leverage.delete(0, tk.END)
            entry_leverage.insert(0, "1")

        # 检查输入值是否合理
        if buy_price <= 0 or sell_price <= 0 or usdt_amount <= 0:
            raise ValueError("所有输入值必须大于零")

        # 计算收益率
        roi = ((sell_price - buy_price) / buy_price) * 100

        # 计算收益额
        profit = usdt_amount * (roi / 100) * leverage

        # 显示结果
        label_profit.config(text=f"收益额: {profit:.2f} USDT")
        label_roi.config(text=f"收益率: {roi:.2f}%")

    except ValueError as e:
        # 弹出错误提示框
        messagebox.showerror("输入错误", str(e))

# 创建主窗口
root = tk.Tk()
root.title("收益率计算器")

# 创建输入框和标签
label_buy_price = tk.Label(root, text="买入价格 (USDT):")
label_buy_price.grid(row=0, column=0, padx=10, pady=10)
entry_buy_price = tk.Entry(root)
entry_buy_price.grid(row=0, column=1, padx=10, pady=10)

label_sell_price = tk.Label(root, text="卖出价格 (USDT):")
label_sell_price.grid(row=1, column=0, padx=10, pady=10)
entry_sell_price = tk.Entry(root)
entry_sell_price.grid(row=1, column=1, padx=10, pady=10)

label_leverage = tk.Label(root, text="杠杆倍数:")
label_leverage.grid(row=2, column=0, padx=10, pady=10)
entry_leverage = tk.Entry(root)
entry_leverage.grid(row=2, column=1, padx=10, pady=10)

label_usdt_amount = tk.Label(root, text="买入 USDT 数量:")
label_usdt_amount.grid(row=3, column=0, padx=10, pady=10)
entry_usdt_amount = tk.Entry(root)
entry_usdt_amount.grid(row=3, column=1, padx=10, pady=10)

# 创建计算按钮
button_calculate = tk.Button(root, text="计算", command=calculate)
button_calculate.grid(row=4, column=0, columnspan=2, pady=10)

# 创建结果标签
label_profit = tk.Label(root, text="收益额: ")
label_profit.grid(row=5, column=0, columnspan=2, pady=10)

label_roi = tk.Label(root, text="收益率: ")
label_roi.grid(row=6, column=0, columnspan=2, pady=10)

# 运行主循环
root.mainloop()
