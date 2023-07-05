from http import HTTPStatus

import pytest

# from backend.foodgram.recipes.models import Ingredient


@pytest.mark.django_db(transaction=True)
class TestIngredientAPI:

    ingredient_url = '/api/ingredients/'
    ingredient_detail_url = '/api/ingredients/{ingredient_id}/'

    def check_ingredient_info(self, ingredient_info, url):
        assert 'id' in ingredient_info, (
            f'Ответ на GET-запрос к `{url}` содержит неполную информацию об '
            'ингредиенте. Проверьте, что поле `id` добавлено в список полей '
            '`fields` сериализатора модели `Ingredient`.'
        )
        assert 'name' in ingredient_info, (
            f'Ответ на GET-запрос к `{url}` содержит неполную информацию об '
            'ингредиенте. Проверьте, что поле `name` добавлено в список полей '
            '`fields` сериализатора модели `Ingredient`.'
        )
        assert 'measurement_unit' in ingredient_info, (
            f'Ответ на GET-запрос к `{url}` содержит неполную информацию о '
            'ингредиенте. Проверьте, что поле `measurement_unit` добавлено в список '
            'полей `fields` сериализатора модели `Ingredient`.'
        )


    def test_ingredient_not_found(self, client, ingredient_1):
        response = client.get(self.ingredient_url)

        assert response.status_code != HTTPStatus.NOT_FOUND, (
            f'Эндпоинт `{self.ingredient_url }` не найден, проверьте настройки в '
            '*urls.py*.'
        )
    # неправильный тест или неправильный код??
    def test_ingredient_list_not_auth(self, client, ingredient_1):
        response = client.get(self.ingredient_url)
        assert response.status_code == HTTPStatus.UNAUTHORIZED, (
            'Проверьте, что GET-запрос неавторизованного пользователя к '
            f'`{self.ingredient_url}` возвращает ответ со статусом 401.'
        )
 

    def test_ingredient_page_not_found(self, client, ingredient_1):
        response = client.get(
            self.ingredient_detail_url.format(ingredient_id=ingredient_1.id)
        )
        assert response.status_code != HTTPStatus.NOT_FOUND, (
            f'Эндпоинт `{self.ingredient_detail_url}` не найден, проверьте '
            'настройки в *urls.py*.'
        )

    # def test_group_single_not_auth(self, client, group_1):
    #     response = client.get(
    #         self.group_detail_url.format(group_id=group_1.id)
    #     )
    #     assert response.status_code == HTTPStatus.OK, (
    #         'Проверьте, что GET-запрос неавторизованного пользователя к '
    #         f'`{self.group_detail_url}` возвращает ответ со статусом 200.'
    #     )

    # def test_group_auth_get(self, user_client, group_1, group_2):
    #     response = user_client.get(self.group_url)
    #     assert response.status_code == HTTPStatus.OK, (
    #         'Проверьте, что для авторизованного пользователя GET-запрос к '
    #         f'{self.group_url}` возвращает ответ со статусом 200.'
    #     )

    #     test_data = response.json()
    #     assert isinstance(test_data, list), (
    #         'Проверьте, что для авторизованного пользователя '
    #         f'GET-запрос к `{self.group_url}` возвращает информацию о группах '
    #         'в виде списка.'
    #     )
    #     assert len(test_data) == Group.objects.count(), (
    #         'Проверьте, что для авторизованного пользователя GET-запрос к '
    #         f'`{self.group_url}` возвращает информацию обо всех существующих '
    #         'группах.'
    #     )

    #     test_group = test_data[0]
    #     self.check_group_info(test_group, self.group_url)

    def test_ingredient_create(self, user_client, ingredient_1, ingredient_2):
        data = {'name': 'Ингредиент 3'}
        response = user_client.post(self.ingredient_url, data=data)
        assert response.status_code == HTTPStatus.METHOD_NOT_ALLOWED, (
            'Убедитесь, что ингредиент можно создавать только через админку и что '
            f'при попытке создать его через POST-запрос к `{self.ingredient_url}` '
            'возвращается статус 405.'
        )

    def test_ingredient_page_auth_get(self, user_client, ingredient_1):
        response = user_client.get(
            self.ingredient_detail_url.format(ingredient_id=ingredient_1.id)
        )
        assert response.status_code == HTTPStatus.OK, (
            'Проверьте, что при GET-запросе авторизованного пользователя к '
            f'`{self.ingredient_detail_url}` возвращается ответ со статусом 200.'
        )

        test_data = response.json()
        assert isinstance(test_data, dict), (
            'Проверьте, что при GET-запросе авторизованного пользователя к '
            f'`{self.ingredient_detail_url}` информация об ингредиенте возвращается в '
            'виде словаря.'
        )
        self.check_ingredient_info(test_data, '/api/ingredients/{ingredient_id}/')