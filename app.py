from flask import Flask, request, render_template, redirect, url_for
import os
from forex_python.converter import CurrencyRates

app = Flask(__name__)

c = CurrencyRates()

@app.route('/', methods=['GET', 'POST'])
def currency_converter():
    """Convert currency and display the conversion result."""
    if request.method == 'POST':
        amount = float(request.form['amount'])
        source_currency = request.form['source_currency'].upper()
        target_currency = request.form['target_currency'].upper()
        try:
            converted_amount = c.convert(source_currency, target_currency, amount)
            return render_template('conversion_result.html', converted_amount=converted_amount,
                                   source_currency=source_currency, target_currency=target_currency)
        except Exception as e:
            return render_template('currency_converter.html', error=str(e))
    return render_template('currency_converter.html')


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
