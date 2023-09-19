from typing import List

from sqlalchemy import String, Numeric, create_engine, select, Text, ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session, relationship

import click
import requests


def get_coin_prices(coins, currencies):
    coin_csv = ",".join(coins)
    currency_csv = ",".join(currencies)

    COINGECKO_URL = f"https://api.coingecko.com/api/v3/simple/price?ids={coin_csv}&vs_currencies={currency_csv}"

    data = requests.get(COINGECKO_URL).json()

    return data


class Base(DeclarativeBase):
    pass


class Portfolio(Base):
    __tablename__ = "portfolio"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(256))
    description: Mapped[str] = mapped_column(Text())

    investments: Mapped[List["Investment"]] = relationship(
        back_populates="portfolio")

    def __repr__(self) -> str:
        return f"<Portfolio name: {self.name} with {len(self.investments)} investment(s)>"


class Investment(Base):
    __tablename__ = "investment"

    id: Mapped[int] = mapped_column(primary_key=True)
    coin: Mapped[str] = mapped_column(String(32))
    currency: Mapped[str] = mapped_column(String(3))
    amount: Mapped[float] = mapped_column(Numeric(5, 2))

    portfolio_id: Mapped[int] = mapped_column(ForeignKey("portfolio.id"))
    portfolio: Mapped["Portfolio"] = relationship(
        back_populates="investments")

    def __repr__(self) -> str:
        return f"<Investment coin: {self.coin}, currency: {self.currency}, amount: {self.amount}>"


# engine = create_engine("sqlite:///manager.db")
engine = create_engine("postgresql://postgres:pgpassword@localhost/manager")
Base.metadata.create_all(engine)


@click.group()
def cli():
    pass


@click.command(help="View the investments in a portfolio")
def view_portfolio():
    with Session(engine) as session:
        stmt = select(Portfolio)
        all_portfolios = session.execute(stmt).scalars().all()

        for index, portfolio in enumerate(all_portfolios):
            print(f"{index + 1}: {portfolio.name}")

        portfolio_id = int(input("Select a portfolio: ")) - 1
        portfolio = all_portfolios[portfolio_id]

        investments = portfolio.investments

        coins = set([investment.coin for investment in investments])
        currencies = set([investment.currency for investment in investments])

        coin_prices = get_coin_prices(coins, currencies)

        print(f"Investments in {portfolio.name}")
        for index, investment in enumerate(investments):
            coin_price = coin_prices[investment.coin][investment.currency.lower(
            )]
            total_price = float(investment.amount) * coin_price
            print(
                f"{index + 1}: {investment.coin} {total_price:.2f} {investment.currency}")

        print("Prices provided by CoinGecko")


@click.command(help="Create a new investment and add it to a portfolio")
@click.option("--coin", prompt=True)
@click.option("--currency", prompt=True)
@click.option("--amount", prompt=True)
def add_investment(coin, currency, amount):
    with Session(engine) as session:
        stmt = select(Portfolio)
        all_portfolios = session.execute(stmt).scalars().all()

        for index, portfolio in enumerate(all_portfolios):
            print(f"{index + 1}: {portfolio.name}")

        portfolio_index = int(input("Select a portfolio: ")) - 1
        portfolio = all_portfolios[portfolio_index]

        investment = Investment(coin=coin, currency=currency, amount=amount)
        portfolio.investments.append(investment)

        session.add(portfolio)
        session.commit()

        print(f"Added new {coin} investment to {portfolio.name}")


@click.command(help="Create a new portfolio")
@click.option("--name", prompt=True)
@click.option("--description", prompt=True)
def add_portfolio(name, description):
    portfolio = Portfolio(name=name, description=description)
    with Session(engine) as session:
        session.add(portfolio)
        session.commit()
    print(f"Added portfolio {name}")


@click.command(help="Drop all tables in the database")
def clear_database():
    Base.metadata.drop_all(engine)
    print("Database cleared!")


cli.add_command(clear_database)
cli.add_command(add_portfolio)
cli.add_command(add_investment)
cli.add_command(view_portfolio)

if __name__ == "__main__":
    cli()
