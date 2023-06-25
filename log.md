Проверка:
 - соответствие кодов ответов
 - наличие предупреждающих сообщений об ошибках
 - соответствие полей и формы вывода ответов
 - permissions
 - запрет невалидных методов(POST, DELETE, etc...)

План:
 - Пользователи
   - Регистрация
     - проверка регистрации с невалидными данными
     - проверка регистрации с валидными данными
     - проверка регистрации с капслоком, email должен быть lower() в базе
   - Список пользователей
     - проверка пагинированного вывода от анонима с лимитом
     - проверка рагинированного вывода от пользователя с лимитом
     - проверка method not allowed на все запросы, кроме GET
   - Профиль пользователя
     - проверка вывода от анонима
     - проверка вывода от пользователя
     - проверка методов
   - Текущий пользователь
     - проверка вывода от анонима
     - проверка вывода от пользователя
     - проверка методов
   - Изменение пароля
     - проверка от анонима
     - проверка от пользователя
     - проверка методов
   - Получение токена
     - проверка ответа от анонима
     - проверка методов
   - Уладение токена
     - проверка ответа от пользователя
     - проверка методов
 - Теги
   - Список тегов
     - проверка вывода от анонима
     - проверка вывода от пользователя
     - проверка методов
   - Получение тега
     - проверка вывода от анонима
     - проверка вывода от пользователя
     - проверка методов
 - Рецепты
   - Список рецептов
     - проверка пагинированного вывода от анонима 
     - проверка пагинированного вывода от пользователя
     - проверка вывода с query params page 2
     - проверка вывода с query params tags 
     - проверка вывода с qp limit
     - проверка вывода с qp is favorited
     - проверка вывода с qp is_in_shopping_cart
     - 
   - Создание рецепта
     - проверка создания от анонима
     - проверка создания с валидными данными от пользователя
     - проверка ошибки при дубликации
     - проверка создания с невалидными данными(без необходимых полей)
   - Получение рецепта
     - проверка вывода для анонима
     - проверка вывода для пользователя
   - Обновление рецепта
     - проверка от анонима
     - проверка обновления с валидными данными от пользователя
     - проверка обновления с валидными данными от автора
     - проверка обновления с невалидными данными
   - Удаление рецепта
     - проверка от анонима
     - проверка от пользователя
     - проверка от автора
 - Список покупок
   - Скачать список покупок 
     - проверка от анонима
     - проверка от пользователя
     - проверка методов
   - Добавить рецепт в список покупок
     - проверка от анонима
     - проверка от пользователя
     - проверка методов(post & delete only)
   - Удалить рецепт из списка покупок
     - проверка от пользователя
 - Избранное
   - Добавить рецепт в избранное
     - проверка от анонима
     - проверка от пользователя
     - проверкм методов(post & delete only)
   - Удалить рецепт из избранного
     - проверка от пользователя
 - Подписки
   - Мои подписки
     - проверка ответа от анонима
     - проверка пагинированного вывода от пользователя
     - проверка пагинированого вывода с query params page,limit,recipe_limit
     - проверка методов
   - Подписаться на пользователя
     - проверка ответа от анонима
     - проверка ответа от пользователя
     - проверка методов(post & delete only)
   - Отписаться от пользователя
     - проверка ответа от пользователя
 - Ингредиенты
   - Список ингредиентов
     - проверка от анонима
     - проверка от пользователя
     - проверка методов
   - Получение ингредиента
     - проверка от анонима
     - проверка от пользователя
     - проверка методов