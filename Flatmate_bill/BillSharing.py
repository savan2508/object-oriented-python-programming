import webbrowser

from fpdf import FPDF


class Bill:
    """
    Object that contains data about a bill, such as total amount
    and period af the bill
    """

    def __init__(self, amount, period):
        self.amount = amount
        self.period = period


def get_flatmates(total_flatmates: int) -> dict:
    flatmates_name = {}
    for i in range(total_flatmates):
        name = input(f"What is the name of the #{i + 1} flatmate? ")
        days = int(input(f"How many days {name} stayed at the house? "))
        flatmates_name[name] = days
    return flatmates_name


def pays(flatmates_name,bill: Bill):
    flatmates_pay = {}
    total_days = sum(flatmates_name.values())

    for i in flatmates_name:
        name = i
        weight = flatmates_name[i] / total_days
        pay = round(bill.amount * weight, 2)
        flatmates_pay[name] = pay
    return flatmates_pay


def generate(flatmates_name, flatmates_pay, bill):
    pdf = FPDF('p', 'pt', 'A4')
    pdf.add_page()

    # insert title
    pdf.set_font(family='Times', size=24, style='B')
    pdf.cell(0, 80, txt='Flatmates Bill', border=0, align='C', ln=1)

    pdf.set_font(family='Times', size=15, style='B')
    pdf.cell(190, 50, txt='Period', border=0)
    pdf.cell(190, 50, txt=bill.period, border=0)
    pdf.cell(190, 50, txt=f'Total Amount = ${bill.amount}', border=0, ln=1)

    pdf.set_font(family='Times', size=12, style='B')
    pdf.cell(100, 25, txt='Name', border=1)
    pdf.cell(150, 25, txt='Amount Owed', border=1)
    pdf.cell(150, 25, txt='Days at house', border=1, ln=1)

    flatmates_name_key = list(flatmates_name.keys())
    flatmates_name_value = list(flatmates_name.values())
    flatmates_pay_value = list(flatmates_pay.values())

    for i in range(len(flatmates_name)):

        pdf.cell(100, 40, txt=f'{flatmates_name_key[i]}', border=1)
        pdf.cell(150, 40, txt=f'${flatmates_pay_value[i]}', border=1)
        pdf.cell(150, 40, txt=f'{flatmates_name_value[i]}', border=1, ln=1)

    pdf.output(f'{bill.period}.pdf')
    webbrowser.open(f'{bill.period}.pdf')


bill_amount = float(input('What is the total amount of the bill? '))
bill_period = input('What is the period of the bill? eg Dec 2021 ')

the_bill = Bill(bill_amount, bill_period)
# the_bill = Bill(120, 'Dec 2021')
total_flatmates = int(input('How many members are in the house? '))
flatmates_name = get_flatmates(total_flatmates)
# print(flatmates_name)
flatmates_pay = pays(flatmates_name,the_bill)
# print(flatmates_pay)
generate(flatmates_name,flatmates_pay,the_bill)
# a = {'a': 1, 'b': 2, 'c': 3}
# b = {'a': 4, 'b': 5, 'c': 6}
# generate(a, b, the_bill)
