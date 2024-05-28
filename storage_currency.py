
import sqlite3
import requests
import time

class CurrencyStorage:
    def __init__(self):
        self.db_file = 'currency.db'
        self.create_table()

    def create_table(self):
        with sqlite3.connect(self.db_file) as conn:
            cursor = conn.cursor()
            cursor.execute('''CREATE TABLE IF NOT EXISTS cache (
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                base_currency TEXT,
                                target_currency TEXT,
                                rate REAL,
                                timestamp INTEGER
                            )''')

    def get_currency_rate(self, base_currency, target_currency):
        with sqlite3.connect(self.db_file) as conn:
            cursor = conn.cursor()
            cursor.execute('''SELECT rate, timestamp FROM cache 
                              WHERE base_currency=? AND target_currency=?''', (base_currency, target_currency))
            result = cursor.fetchone()
            if result:
                rate, timestamp = result
                if time.time() - timestamp <= 86400:  # 24 horas em segundos
                    return rate

            # Se não houver cache válido ou não encontrado, buscar na API
            api_url = f"https://api.exchangerate-api.com/v4/latest/{base_currency}"
            response = requests.get(api_url)
            data = response.json()
            rate = data['rates'].get(target_currency)
            if rate:
                # Atualizar ou inserir no cache
                cursor.execute('''INSERT OR REPLACE INTO cache 
                                  (base_currency, target_currency, rate, timestamp) 
                                  VALUES (?, ?, ?, ?)''', (base_currency, target_currency, rate, time.time()))
                return rate
            else:
                return None

    