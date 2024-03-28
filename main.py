from tkinter import *

window = Tk()
window.title("Mile converter")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)


def show_result():
    km_result = 1.6 * float(mile_input.get())
    result_label.config(text=f"{km_result:.2f}")



mile_input = Entry()
mile_input.grid(column=1, row=0)


miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

eq_label = Label(text="is equal to")
eq_label.grid(column=0, row=1)

result_label = Label(text="0")
result_label.grid(column=1, row=1)

km_label = Label(text="Km")
km_label.grid(column=2, row=1)

calculate_button = Button(text="Calculate", command=show_result)
calculate_button.grid(column=1, row=2)







window.mainloop()
