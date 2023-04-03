from flask import Flask, request, render_template, redirect, url_for
import os
from forex_python.converter import CurrencyRates

app = Flask(__name__)

c = CurrencyRates()

@app.route('/', methods=['GET', 'POST'])
def currency_converter():
    if request.method == 'POST':
        amount = float(request.form['amount'])
        target_currency = request.form['currency']
        converted_amount = c.convert('USD', target_currency, amount)
        return render_template('conversion_result.html', converted_amount=converted_amount)
    return render_template('currency_converter.html')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
