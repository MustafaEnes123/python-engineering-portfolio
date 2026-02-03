import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import json
import os

class MarketDataFetcher:
    def __init__(self):
        self.api_url = "https://api.exchangerate-api.com/v4/latest/USD"
    def fetch_exchange_rate(self):
        try:
            response = requests.get(self.api_url)
            if response.status_code == 200:
                return response.json()['rates']['TRY']
            return 30.5
        except:
            return 30.5
    def fetch_finance_news(self):
        try:
            url = "https://news.google.com/search?q=economy&hl=en-US&gl=US"
            headers = {'User-Agent': 'Mozilla/5.0'}
            response = requests.get(url, headers=headers)
            soup = BeautifulSoup(response.text, 'html.parser')
            headlines = [h.text for h in soup.find_all('a', class_='J77u8')[:5]]
            return headlines
        except:
            return ["Could not fetch news headlines."]
class ExpenseEngine:
    def __init__(self, storage_file='finance_data.json'):
        self.storage_file = storage_file
        self.records = self.load_data()

    def load_data(self):
        if os.path.exists(self.storage_file):
            with open(self.storage_file, 'r') as file:
                return json.load(file)
        return []

    def add_record(self, category, amount_try, detail, rate):
        entry = {
            'category': category,
            'try_amount': amount_try,
            'usd_amount': round(amount_try / rate, 2),
            'description': detail
        }
        self.records.append(entry)
        self.save_data()

    def save_data(self):
        with open(self.storage_file, 'w') as file:
            json.dump(self.records, file, indent=4)

class FinanceDashboard:
    @staticmethod
    def generate_charts(data):
        if not data:
            return
        
        df = pd.DataFrame(data)
        sns.set_theme(style="darkgrid")
        
        plt.figure(figsize=(12, 6))
        df.groupby('category')['try_amount'].sum().plot(kind='pie', autopct='%1.1f%%')
        plt.title("Expense Distribution by Category")
        plt.savefig('expense_pie_chart.png')
        
        plt.figure(figsize=(12, 6))
        sns.barplot(x='category', y='try_amount', data=df, palette='magma')
        plt.title("Total Spending per Category (TRY)")
        plt.savefig('expense_bar_chart.png')
        print("Charts generated: expense_pie_chart.png, expense_bar_chart.png")

class GlobalFinanceIntelligence:
    def __init__(self):
        self.fetcher = MarketDataFetcher()
        self.engine = ExpenseEngine()
        self.current_rate = self.fetcher.fetch_exchange_rate()

    def start(self):
        while True:
            print(f"\n--- GLOBAL FINANCE INTELLIGENCE (1 USD = {self.current_rate} TRY) ---")
            print("1. Add New Expense")
            print("2. Display All Records")
            print("3. Fetch Market News")
            print("4. Generate Dashboard")
            print("5. Exit")
            
            user_input = input("Selection: ")
            
            if user_input == '1':
                cat = input("Category: ")
                amt = float(input("Amount (TRY): "))
                desc = input("Description: ")
                self.engine.add_record(cat, amt, desc, self.current_rate)
            
            elif user_input == '2':
                for r in self.engine.records:
                    print(f"[{r['category']}] {r['try_amount']} TRY / {r['usd_amount']} USD - {r['description']}")
            
            elif user_input == '3':
                news_list = self.fetcher.fetch_finance_news()
                for i, news in enumerate(news_list, 1):
                    print(f"{i}. {news}")
            
            elif user_input == '4':
                FinanceDashboard.generate_charts(self.engine.records)
            
            elif user_input == '5':
                break

if __name__ == "__main__":
    app = GlobalFinanceIntelligence()
    app.start()