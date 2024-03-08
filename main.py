# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

import tkinter as tk

def calculate_interest():
    deposit_amount = float(entry.get())
    if deposit_amount < 100:
        interest_rate = 0.05
    elif 100 <= deposit_amount <= 200:
        interest_rate = 0.07
    else:
        interest_rate = 0.10

    total_amount = deposit_amount + (deposit_amount * interest_rate)
    result_label.config(text=f"Общая сумма с начисленными процентами: {total_amount}")


# Создание графического интерфейса
root = tk.Tk()
root.title("Расчет процентов по вкладу")

label = tk.Label(root, text="Введите сумму вклада:")
label.pack(pady=10)

entry = tk.Entry(root)
entry.pack()

calculate_button = tk.Button(root, text="Рассчитать", command=calculate_interest)
calculate_button.pack(pady=5)

result_label = tk.Label(root, text="")
result_label.pack(pady=10)

root.mainloop()