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
    def test_init_books_genre_is_empty_dict(self, collector):
        assert collector.get_books_genre() == {} #проверяю, что словарь books_genre пустой

    def test_init_favorites_is_empty_list(self, collector):

        assert collector.get_list_of_favorites_books() == [] #проверяю, что список favorites пустой

    def test_init_genre_has_five_elements(self, collector):

        collector.add_new_book('Книга')
    
        for genre in collector.genre:
            collector.set_book_genre('Книга', genre)
            assert collector.get_book_genre('Книга') == genre 
            
    def test_init_genre_contains_fantasy(self, collector):

        collector.add_new_book('Книга')
        collector.set_book_genre('Книга', 'Фантастика')
        assert collector.get_book_genre('Книга') == 'Фантастика' #проверяю, что заявленный жанр есть списке genre

    def test_init_genre_age_rating_is_not_empty(self, collector):

        collector.add_new_book('Книга') 
        age_rating_genres = collector.genre_age_rating 
        assert len(age_rating_genres) > 0 #проверяю, что список genre_age_rating не пустой

    def test_init_genre_age_rating_contains_horror(self, collector):

        collector.add_new_book('Книга')
        collector.set_book_genre('Книга', 'Ужасы')
        assert collector.get_book_genre('Книга') == 'Ужасы' #проверяю, что заявленный жанр есть списке genre_age_rating
    
    def test_add_new_book_with_empty_name_not_added(self, collector):

        collector.add_new_book('') #проверяю, что книга с пустым названием не добавляется
        assert collector.books_genre == {}

    def test_add_new_book_duplicate_not_added(self, collector):

        collector.add_new_book('Мастер и Маргарита')
        collector.add_new_book('Мастер и Маргарита')
        assert len(collector.get_books_genre()) == 1 # Проверяю, что книга только одна

    # Невалидные значения
    @pytest.mark.parametrize('name', [
        '',        # 0 символов
        'A' * 41,  # 41 символ
    ])

    def test_add_new_book_invalid_name_length_not_added(self, name, collector):
        collector.add_new_book(name)
        assert name not in collector.get_books_genre()
        assert collector.get_books_genre() == {}

    # Граничные валидные значения
    @pytest.mark.parametrize('name', [
        'A',        # 1 символ
        'A' * 40,   # 40 символов
    ])

    def test_add_new_book_boundary_valid_name_length_added(self, name, collector):
        collector.add_new_book(name)
        assert name in collector.get_books_genre()
        assert collector.get_books_genre()[name] == ''

    @pytest.mark.parametrize('book_name, genre', [
    ('Книга1', 'Фантастика'),
    ('Книга2', 'Ужасы')])

    def test_get_book_genre_for_existing_book(self, book_name, genre, collector):

        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, genre)
        result = collector.get_book_genre(book_name)
        assert result == genre

    @pytest.mark.parametrize('books_to_add, genre, expected_books', [
    ([('Книга1', 'Фантастика')], 'Фантастика', ['Книга1']),
    ([('Книга2', 'Ужасы')], 'Ужасы', ['Книга2']),
    ([('Книга3', 'Детективы'), ('Книга4', 'Детективы')], 'Детективы', ['Книга3', 'Книга4'])])

    def test_get_books_with_specific_genre_existing_genres(self, books_to_add, genre, expected_books, collector):
        for book_name, book_genre in books_to_add:
            collector.add_new_book(book_name)
            collector.set_book_genre(book_name, book_genre)
    
        result = collector.get_books_with_specific_genre(genre)
        assert result == expected_books

    def test_get_books_genre_returns_not_empty_dict(self, collector):

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

    def test_get_books_for_children_returns_safe_genres(self, book_name, genre, collector):

        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, genre)
    
        result = collector.get_books_for_children()
        assert book_name in result

    def test_add_book_in_favorites_single_book(self, collector):
        book_name = 'Фантастика книга'
        collector.add_new_book(book_name)
        collector.add_book_in_favorites(book_name)
        assert book_name in collector.get_list_of_favorites_books() 

    def test_delete_book_from_favorites_existing_book(self, collector):

        collector.add_new_book('Книга')
        collector.add_book_in_favorites('Книга')
        collector.delete_book_from_favorites('Книга')
        assert collector.favorites == []

    def test_get_list_of_favorites_books_add_two_books(self, collector):

        collector.add_new_book('Книга1')
        collector.add_new_book('Книга2')
        collector.add_book_in_favorites('Книга1')
        collector.add_book_in_favorites('Книга2')
        assert collector.get_list_of_favorites_books() == ['Книга1', 'Книга2']
