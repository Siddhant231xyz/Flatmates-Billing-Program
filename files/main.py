from fpdf import FPDF
import webbrowser
import time
class Bill():
    def __init__(self, amount, period):
        self.amount = amount
        self.period = period

class Flatemate():
    def __init__(self, name, days_in_house):
        self.name = name
        self.days_in_house = days_in_house

    def pays(self, bill, flatmate2):
        weight = self.days_in_house / (self.days_in_house + flatmate2.days_in_house)
        to_pay = bill.amount*weight
        return to_pay

class PdfReport():
    def __init__(self, filename):
        self.filename = filename

    def generate(self, flatmate1, flatmate2, bill):

        pdf = FPDF(orientation='P', unit='pt', format='A4')
        pdf.add_page()

        pdf.image("house.png", w=30, h=30)

        pdf.set_font(family='Times', size=24, style='B')

        pdf.cell(w=0, h=80, txt="Flatmates-Bill", border=0, align="C", ln=1)

        pdf.set_font(family='Times', size=14, style='B')
        pdf.cell(w=100, h=40, txt='Period', border=0)
        pdf.cell(w=150, h=40, txt=bill.period, border=0, ln=1)

        pdf.set_font(family='Times', size=12)

        pdf.cell(w=100, h=40, txt=flatmate1.name, border=0)
        pdf.cell(w=150, h=40, txt=str(round(flatmate1.pays(bill,flatmate2),2)), border=0, ln=1)

        pdf.cell(w=100,h=40, txt=flatmate2.name, border=0)
        pdf.cell(w=150,h=40, txt=str(round(flatmate2.pays(bill,flatmate1),2)),border=0)


        pdf.output(self.filename)
        webbrowser.open(self.filename)

print("This is an App to find out the billing amount to be paid between two Flatmates")
time.sleep(2)
a = float(input("Enter the Bill amount: "))
b = input("Enter the Period: E.g November 2020 ")
c = input("Enter the Flatmate 1 Name: ")
e = float(input("How many days flatmate1 lived? "))
d = input("Enter the Flatmate 2 Name: ")
f = float(input("How many days flatmate2 lived? "))


bill = Bill(amount=a, period = b)
flatmate1 = Flatemate(name=c, days_in_house=e)
flatmate2 = Flatemate(name=d, days_in_house=f)
print("John Pays:", flatmate1.pays(bill, flatmate2))
print("Marry Pays: ", flatmate1.pays(bill, flatmate1))

pdf = PdfReport(filename ="report1.pdf")
pdf.generate(flatmate1, flatmate2, bill=bill)