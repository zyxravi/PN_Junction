from tkinter import *
import math

# root window
root = Tk()
root.minsize(width=500, height=800)
root.config(background="gray")

# pn junction image setup
img = PhotoImage(name="PN Junction", file="unbiased-P-N-junction.png")
panel = Label(root, image=img)
panel.grid(row=0, column=2)

# Notation Information
notation_text1 = ("Information:\nHere acceptor and donor value are in term of 1e__ ,\nplease provide the value of "
                  "power only")
notation1 = Label(root, text=notation_text1, bg="aqua")
notation1.grid(row=1, column=2)
notation_text2 = "Eg. If you want value 1e14, then only insert 14 . "
notation2 = Label(root, text=notation_text2, bg="aqua")
notation2.grid(row=2, column=2)
# Acceptor Label
acceptor = Label(root, text="acceptor concentration")
acceptor.grid(row=3, column=0)
# acceptor.config(width=20, height=1)

# acceptor entry
a_value = StringVar(root)
acceptor_entry = Entry(root, textvariable=a_value)
acceptor_entry.grid(row=3, column=1)

# donor label
donor = Label(root, text="donor concentration")
donor.grid(row=3, column=4)
# donor.config(width=20, height=1)

# donor entry
d_value = StringVar(root)
donor_entry = Entry(root, textvariable=d_value)
donor_entry.grid(row=3, column=5)

# Biasing data
text_asking = "Are you doing biasing? \n If yes, Enter Biasing Voltage.\n otherwise leave blank."
asking = Label(root, text=text_asking, bg="aqua")
asking.grid(row=4, column=2)

biasing_value = StringVar(root)
biasing = Entry(root, textvariable=biasing_value)
biasing.grid(row=5, column=2)


# clearing content
def clear_text():
    biasing.delete(0, END)
    donor_entry.delete(0, END)
    acceptor_entry.delete(0, END)


# hard data
Ni = pow(10, 10)
Eg = 1.12
Nc = 2.8 * pow(10, 19)
Nv = 1.04 * pow(10, 19)
Electron_Affinity = 4.05
T = 300
permittivity = 11.2 * 8.85 * pow(10, -14)
thermal_voltage = 0.026
q = 1.6 * pow(10, -19)
Io = 5 * pow(10, -12)
e = 2.71828


# calculation function
def calculation():
    Va = float(biasing_value.get()) if float(biasing_value.get()) else 0
    Nd = pow(10, float(d_value.get()))
    Na = pow(10, float(a_value.get()))
    # common calculation
    print(Va)
    Vbi = thermal_voltage * math.log(Na * Nd / (Ni * Ni), e)
    Width = math.sqrt(2 * permittivity * (Vbi - Va) * (Na + Nd) / (1.6 * pow(10, -19) * (Na + Nd))) if Va < Vbi else 0
    mobility_electron = (88 * pow(T / 300, -0.57) + (7.4 * pow(10, 8) * pow(T, -2.33)) / (
            1 + 0.88 * Nd * pow(T / 300, -0.146) / (1.26 * pow(10, 17) * pow(T / 300, 2.4))))
    mobility_hole = (54.3 * pow(T / 300, -0.57) + (1.36 * pow(10, 8) * pow(T, -2.33)) / (
            1 + 0.88 * Na * pow(T / 300, -0.146) / (2.35 * pow(10, 17) * pow(T / 300, 2.4))))
    c_forward = permittivity / math.sqrt(2 * q * (Na + Nd) * (Va - Vbi))
    cpu = math.sqrt(q * Nd * permittivity / (2 * (Vbi - Va))) if Va < Vbi else c_forward
    # current = Io * (pow(e, Va / thermal_voltage) - 1)
    common_data_text = (f"Built-in potential: {Vbi}\nDepletion Width: {Width}\nElectron Mobility: {mobility_electron}\n"
                        f"Hole Mobility: {mobility_hole}\n Capacitance Per Unit Area: {cpu}\n ")
    common = Label(root, text=common_data_text)
    common.grid(row=6, column=2)
    # P side carrier concentration
    p_holes = f"Holes in P side : 1E{float(a_value.get())}"
    p_electron = f"Electrons in P side: 1E{20 - float(a_value.get())}"

    p_text = f"mobility of hole: {p_holes} \n{p_electron}"
    P_label = Label(root, text=p_text)
    P_label.grid(row=5, column=0)

    # N side carrier concentration
    n_holes = f"Holes in P side : 1E{float(d_value.get())}"
    n_electron = f"Electrons in P side: 1E{20 - float(d_value.get())}"

    n_text = f"mobility of electron : {n_holes}\n{n_electron}"
    N_label = Label(root, text=n_text)
    N_label.grid(row=5, column=3)
    # for clearing all contents
    clear_button = Button(root, text="Clear", command=clear_text, bg="red")
    clear_button.grid(row=8, column=2)


# submit button to calculate data
submit_button = Button(root, text="Submit", command=calculation, bg="#90EE90")
submit_button.grid(row=7, column=2)

root.mainloop()
