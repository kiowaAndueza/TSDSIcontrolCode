from tkinter import *
from controlCode import calculate_check_digits

class Application(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("Calculadora para el código de control de facturas eléctricas")
        self.create_widgets()

    def create_widgets(self):
        self.distributor_label = Label(self.master, text="Inserta los 4 dígitos del distribuidor: ")
        self.distributor_label.grid(row=0, column=0, sticky=W)

        self.distributor_entry = Entry(self.master)
        self.distributor_entry.grid(row=0, column=1)

        self.assignment_label = Label(self.master, text="Inserta los 12 dígitos de libre elección asociados a la factura: ")
        self.assignment_label.grid(row=1, column=0, sticky=W)

        self.assignment_entry = Entry(self.master)
        self.assignment_entry.grid(row=1, column=1)

        self.calculate_button = Button(self.master, text="Calcular código de control", command=self.calculate)
        self.calculate_button.grid(row=2, column=0, columnspan=2, pady=10)

        self.result_label = Label(self.master, text="")
        self.result_label.grid(row=3, column=0, columnspan=2)

    def calculate(self):
        distributor = self.distributor_entry.get()
        free_assignment = self.assignment_entry.get()

        check_digits = calculate_check_digits(distributor, free_assignment)

        self.result_label.config(text=f"El código de control es: {check_digits}")


if __name__ == "__main__":
    root = Tk()
    app = Application(master=root)
    app.mainloop()
