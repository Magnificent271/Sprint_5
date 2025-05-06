import pytest
from main import BooksCollector

@pytest.fixture  #Фикстура создания экземпляра BooksCollector
def collector():
    collector = BooksCollector()
    return collector
