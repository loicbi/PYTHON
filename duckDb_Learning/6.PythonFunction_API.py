import duckdb

from duckdb.typing import *
from faker import Faker


def random_name():
    fake = Faker()
    return fake.name()


# print(random_name())

duckdb.create_function('random_name', random_name, [], VARCHAR)
res = duckdb.sql('select random_name()').fetchall()
print(res)


def my_function(x: int) -> str:
    return x

duckdb.create_function('my_function', my_function)
duckdb.sql('SELECT my_function(8485)').show()
