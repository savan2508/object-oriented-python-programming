from flask import Flask, render_template, request
from flask.views import MethodView
from wtforms import Form, StringField, SubmitField
import flat

app = Flask(__name__)


class HomePage(MethodView):

    def get(self):
        return render_template('index.html')


class BillFormPage(MethodView):

    def get(self):
        bill_form = BillForm()
        return render_template('bill_form_page.html',
                               billform=bill_form)


class ResultsPage(MethodView):

    def post(self):
        billform = BillForm(request.form)
        amount = float(billform.amount.data)
        period = billform.period.data

        name1 = billform.name1.data
        day_in_house1 = float(billform.days_in_house1.data)

        name2 = billform.name2.data
        day_in_house2 = float(billform.days_in_house2.data)

        the_bill = flat.Bill(amount=amount, period=period)
        flatmate1 = flat.Flatmate(name=name1, days_in_house=day_in_house1)
        flatmate2 = flat.Flatmate(name=name2, days_in_house=day_in_house2)

        return render_template('bill_result.html',
                               name1=flatmate1.name,
                               amount1=flatmate1.pays(the_bill, flatmate2),
                               name2=flatmate2.name,
                               amount2=flatmate2.pays(the_bill, flatmate1))


class BillForm(Form):
    amount = StringField("Bill Amount: ")
    period = StringField("Bill Period: ")

    name1 = StringField('Name: ')
    days_in_house1 = StringField('Days in the House: ')

    name2 = StringField('Name: ')
    days_in_house2 = StringField('Days in the House: ')

    button = SubmitField("Calculate")


app.add_url_rule('/',
                 view_func=HomePage.as_view('home_page'))
app.add_url_rule('/bill_form',
                 view_func=BillFormPage.as_view('bill_form_page'))
app.add_url_rule('/bill_result', view_func=ResultsPage.as_view('results_page'))

app.run(debug=True)
