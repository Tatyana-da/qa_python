# qa_python
Список тестов
1. test_init_books_genre_is_empty_dict - При создании объекта словарь books_genre пустой
2. test_init_favorites_is_empty_list - При создании объекта список favorites пустой
3. test_init_genre_has_five_elements - Список genre содержит 5 жанров
4. test_init_genre_contains_fantasy - Жанр 'Фантастика' присутствует в списке genre
5. test_init_genre_age_rating_is_not_empty - Список genre_age_rating не пустой
6. test_init_genre_age_rating_contains_horror - Жанр 'Ужасы' присутствует в списке genre_age_rating
7. test_add_new_book_add_two_books - Добавление двух книг увеличивает словарь до 2 элементов
8. test_add_new_book_with_empty_name_not_added - Книга с пустым названием не добавляется
9. test_add_new_book_duplicate_not_added - Одинаковую книгу нельзя добавить дважды
10. test_set_book_genre_expected_genres - Установка жанра для книги (проверка всех 5 жанров)
11. test_get_book_genre_for_existing_book - Получение жанра существующей книги 
12. test_get_books_with_specific_genre_existing_genres - Получение списка книг по жанру с проверкой нескольких книг одного жанра
13. test_get_books_genre_returns_not_empty_dict - Метод get_books_genre() возвращает правильный словарь с книгами и жанрами
14. test_get_books_for_children_returns_safe_genres - Получение книг без возрастного рейтинга 
15. test_add_book_in_favorites_several_books - Добавление нескольких книг в избранное
16. test_delete_book_from_favorites_existing_book - Удаление книги из избранного
17. test_get_list_of_favorites_books_add_two_books - Получение списка избранных книг после добавления двух книг