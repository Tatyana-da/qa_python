import pytest
from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_genre()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector
    def test_init_books_genre_is_empty_dict(self):
        collector = BooksCollector()
        assert collector.books_genre == {} #проверяю, что словарь books_genre пустой

    def test_init_favorites_is_empty_list(self):
        collector = BooksCollector()
        assert collector.favorites == [] #проверяю, что список favorites пустой

    def test_init_genre_has_five_elements(self):
        collector = BooksCollector()
        assert len(collector.genre) == 5  #проверяю, что список genre НЕ пустой  

    def test_init_genre_contains_fantasy(self):
        collector = BooksCollector()
        assert 'Фантастика' in collector.genre #проверяю, что заявленный жанр есть списке genre

    def test_init_genre_age_rating_is_not_empty(self):
        collector = BooksCollector()
        assert len(collector.genre_age_rating) > 0 #проверяю, что список genre_age_rating не пустой

    def test_init_genre_age_rating_contains_horror(self):
        collector = BooksCollector()
        assert 'Ужасы' in collector.genre_age_rating #проверяю, что заявленный жанр есть списке genre_age_rating
    
    def test_add_new_book_with_empty_name_not_added(self):
        collector = BooksCollector()
        collector.add_new_book('') #проверяю, что книга с пустым названием не добавляется
        assert collector.books_genre == {}

    def test_add_new_book_duplicate_not_added(self):
        collector = BooksCollector()
        collector.add_new_book('Мастер и Маргарита')
        collector.add_new_book('Мастер и Маргарита')
        assert len(collector.books_genre) == 1 # Проверяю, что книга только одна

    @pytest.mark.parametrize('book_name, genre, expected_genre', [
        ('Книга1', 'Фантастика', 'Фантастика'),
        ('Книга2', 'Ужасы', 'Ужасы'),
        ('Книга3', 'Детективы', 'Детективы'),
        ('Книга4', 'Мультфильмы', 'Мультфильмы'),
        ('Книга5', 'Комедии', 'Комедии')])
    
    def test_set_book_genre_expected_genres(self, book_name, genre, expected_genre):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, genre)
        assert collector.get_book_genre(book_name) == expected_genre

    @pytest.mark.parametrize('book_name, genre', [
    ('Книга1', 'Фантастика'),
    ('Книга2', 'Ужасы')])

    def test_get_book_genre_for_existing_book(self, book_name, genre):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, genre)
        result = collector.get_book_genre(book_name)
        assert result == genre

    @pytest.mark.parametrize('genre, expected_books', [
    ('Фантастика', ['Книга1']),
    ('Ужасы', ['Книга2']),
    ('Детективы', ['Книга3', 'Книга4'])])  # хотела добавить проверку на несколько книг одного жанра

    def test_get_books_with_specific_genre_existing_genres(self, genre, expected_books):
        collector = BooksCollector()
        collector.add_new_book('Книга1')
        collector.set_book_genre('Книга1', 'Фантастика')
        collector.add_new_book('Книга2')
        collector.set_book_genre('Книга2', 'Ужасы')
        collector.add_new_book('Книга3')
        collector.set_book_genre('Книга3', 'Детективы')
        collector.add_new_book('Книга4')
        collector.set_book_genre('Книга4', 'Детективы')
    
        result = collector.get_books_with_specific_genre(genre)
        assert result == expected_books

    def test_get_books_genre_returns_not_empty_dict(self):
        collector = BooksCollector()
        collector.add_new_book('Книга1')
        collector.set_book_genre('Книга1', 'Фантастика')
        collector.add_new_book('Книга2')
        collector.set_book_genre('Книга2', 'Ужасы')
    
        expected = {
            'Книга1': 'Фантастика',
            'Книга2': 'Ужасы'
        }
        assert collector.get_books_genre() == expected

    @pytest.mark.parametrize('book_name, genre', [
    ('Фантастика книга', 'Фантастика'),
    ('Комедия книга', 'Комедии'),
    ('Мультфильм книга', 'Мультфильмы')])

    def test_get_books_for_children_returns_safe_genres(self, book_name, genre):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, genre)
    
        result = collector.get_books_for_children()
        assert book_name in result

    @pytest.mark.parametrize('book_name', [
        'Фантастика книга',
        'Ужасы книга',
        'Детектив книга'
    ])
    def test_add_book_in_favorites_several_books(self, book_name):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        collector.add_book_in_favorites(book_name)
        assert book_name in collector.favorites 

    def test_delete_book_from_favorites_existing_book(self):
        collector = BooksCollector()
        collector.add_new_book('Книга')
        collector.add_book_in_favorites('Книга')
        collector.delete_book_from_favorites('Книга')
        assert collector.favorites == []

    def test_get_list_of_favorites_books_add_two_books(self):
        collector = BooksCollector()
        collector.add_new_book('Книга1')
        collector.add_new_book('Книга2')
        collector.add_book_in_favorites('Книга1')
        collector.add_book_in_favorites('Книга2')
        assert collector.get_list_of_favorites_books() == ['Книга1', 'Книга2']
