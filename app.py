from flask import Flask
import os
from forex_python.converter import CurrencyRates
from flask import request, render_template

app = Flask(__name__)

c = CurrencyRates()

@app.route('/currency_converter')
def currency_converter():
    return render_template('currency_converter.html')

@app.route('/convert_currency', methods=['POST'])
def convert_currency():
    amount = float(request.form['amount'])
    target_currency = request.form['currency']
    converted_amount = c.convert('USD', target_currency, amount)
    return render_template('conversion_result.html', converted_amount=converted_amount)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
