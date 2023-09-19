from dataclasses import dataclass
import csv

import click
import requests
import psycopg
import datetime

@dataclass
class Investment:
    coin_id: str
    currency: str
    amount: float
    sell: bool
    date: datetime.datetime

def get_connection():
    connection = psycopg.connect(
        host="localhost",
        dbname="manager",
        user="postgres",
        password="mysecretpassword"
    )

    return connection

@click.group()
def cli():
    pass

@click.command()
@click.option("--coin", prompt=True)
@click.option("--currency", prompt=True)
@click.option("--amount", prompt=True)
def new_investment(coin, currency, amount):
    stmt = f"""
        insert into investments (
            coin_id, currency, amount
        ) values (
            '{coin.lower()}', '{currency.lower()}', {amount}
        )
    """

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(stmt)
    connection.commit()

    cursor.close()
    connection.close()
    
    print(f"Added investment for {amount} {coin} in {currency}")


@click.command()
@click.option("--currency")
def view_investments(currency):
    connection = get_connection()
    cursor = connection.cursor()

    stmt = "select * from investments"

    if currency is not None:
        stmt += f" where currency='{currency.lower()}'"

    cursor.execute(stmt)
    # data = [Investment(**dict(row)) for row in cursor.fetchall()]
    data = cursor.fetchall()

    cursor.close()
    connection.close()

    print(data)

    # coins = set([row.coin for row in data])
    # currencies = set([row.currency for row in data])

    # url = f"https://api.coingecko.com/api/v3/simple/price?ids={','.join(coins)}&vs_currencies={','.join(currencies)}"
    # coin_data = requests.get(url).json()

    # for investment in data:
    #     coin_price = coin_data[investment.coin][investment.currency.lower()]
    #     coin_total = investment.amount * coin_price
    #     print(f"{investment.amount} {investment.coin} in {investment.currency} is worth {coin_total}")

cli.add_command(view_investments)
cli.add_command(new_investment)

if __name__ == "__main__":
    cli()
