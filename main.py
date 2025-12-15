from tkinter import *

FONT = ("Ariel", 14)
PAD_Y = 16

def convert_miles_to_kilometers():
    miles = entry_miles.get()
    kilometers = float(miles) * 1.609344
    label_km_value.config(text=f"{kilometers}")

# Setup main window
window = Tk()
window.title("Miles to Kilometers Converter")
window.minsize(width=400, height=200)
window.config(padx=30, pady=30)

# Entry field for miles input
entry_miles = Entry(width=10, font=FONT)
entry_miles.grid(column=1, row=0)

# Miles label
label_miles = Label(text="Miles", font=FONT)
label_miles.grid(column=2, row=0)

# "Is equal to" label
label_equal = Label(text="is equal to", font=FONT)
label_equal.grid(column=0, row=1)
label_equal.config(pady=PAD_Y)

# Kilometers result label
label_km_value = Label(text=f"{0}", font=FONT)
label_km_value.grid(column=1, row=1)
label_km_value.config(pady=PAD_Y)

# Km label
label_km = Label(text="Km", font=FONT)
label_km.grid(column=2, row=1)
label_km.config(pady=PAD_Y)

# Calculate button
button_calculate = Button(text="Calculate", font=("Ariel", 12), command=convert_miles_to_kilometers)
button_calculate.grid(column=1, row=2)

window.mainloop()
