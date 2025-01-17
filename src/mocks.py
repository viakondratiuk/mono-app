import random
from datetime import date, time
from decimal import Decimal

from faker import Faker
from polyfactory.factories.pydantic_factory import ModelFactory

from .models import Account, Category, Transaction

fake = Faker()


class AccountFactory(ModelFactory[Account]):
    __model__ = Account

    @staticmethod
    def id() -> str:
        return str(fake.uuid4())

    @staticmethod
    def name() -> str:
        return fake.company()

    @staticmethod
    def balance() -> Decimal:
        return Decimal(f"{random.uniform(1000, 10000):.2f}")

    @staticmethod
    def currency() -> str:
        return fake.currency_code()


class CategoryFactory(ModelFactory[Category]):
    __model__ = Category

    @staticmethod
    def id() -> str:
        return str(fake.uuid4())

    @staticmethod
    def name() -> str:
        return fake.word()

    @staticmethod
    def parent_id() -> str | None:
        return random.choice([None, str(fake.uuid4())])


class TransactionFactory(ModelFactory[Transaction]):
    __model__ = Transaction

    @staticmethod
    def date() -> date:
        return fake.date_this_year()

    @staticmethod
    def time() -> time:
        return fake.time_object()

    @staticmethod
    def amount() -> Decimal:
        return Decimal(f"{random.uniform(-500, 500):.2f}")

    @staticmethod
    def account() -> Account:
        return AccountFactory.build()

    @staticmethod
    def category() -> Category:
        return CategoryFactory.build()

    @staticmethod
    def description() -> str:
        return fake.text()
