from flask import Flask, request, jsonify
from flask_caching import Cache
import requests

app = Flask(__name__)

# Configurações para o Flask-Caching
app.config['CACHE_TYPE'] = 'simple'
app.config['CACHE_DEFAULT_TIMEOUT'] = 86400  # 1 dia em segundos

cache = Cache(app)

# Moedas permitidas para cotação
allowed_currencies = ['EUR', 'USD', 'GBP', 'CNY']

# Função para obter a cotação de uma moeda específica
def get_currency_rate(base_currency, target_currency):
    api_url = f"https://api.exchangerate-api.com/v4/latest/{base_currency}"
    response = requests.get(api_url)
    data = response.json()
    rate = data['rates'].get(target_currency)
    return rate

# Rota para obter a cotação de uma moeda específica
@app.route('/currency')
@cache.cached()
def currency():
    base_currency = request.args.get('base', 'BRL')
    target_currency = request.args.get('target')
    
    # Verifica se a moeda de destino está entre as permitidas
    if target_currency and target_currency in allowed_currencies:
        rate = get_currency_rate(base_currency, target_currency)
        if rate:
            return jsonify({f"{base_currency} x {target_currency}": rate})
        else:
            return jsonify({"error": "Moeda não encontrada"}), 404
    elif not target_currency:
        # Retorna as cotações de todas as moedas permitidas
        rates = {f"{base_currency} x {currency}": get_currency_rate(base_currency, currency) for currency in allowed_currencies}
        return jsonify(rates)
    else:
        return jsonify({"error": "Moeda não permitida"}), 400

if __name__ == '__main__':
    app.run(debug=True)
