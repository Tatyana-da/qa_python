import pytest
from main import BooksCollector

@pytest.fixture
def collector():
    collector = BooksCollector()
    yield collector
    collector.books_genre.clear()
    collector.favorites.clear()
