def currency_converter(amount, from_currency, to_currency):
    rates = {
        "USD" : 1.0,
        "INR" : 83.2,
        "EUR" :0.92,
        "GBP" :0.78,
        "JPY" :157.3
    }
    if from_currency not in rates or to_currency not in rates:
        return "Currency not supported."
    usd_amount = amount / rates[from_currency]
    converted_amount = usd_amount * rates[to_currency]
    return  round(converted_amount, 2)

print("=== Currency Converter ===")
amount = float(input("Enter the amount to convert: "))
from_currency = input("From Currency (e.g., USD, INR): ").upper()
to_currency = input("To currency (e.g., USD, INR): ").upper()

result =currency_converter(amount, from_currency, to_currency)
print(f"\n{amount} {from_currency} = {result} {to_currency}")