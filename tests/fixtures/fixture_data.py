import pytest
import tempfile

from recipes.models import Ingredient, Tag, Recipe

@pytest.fixture
def ingredient_1():
    return Ingredient.objects.create(
        name='Ингредиент_1', 
        measurement_unit='measurement_unit_1'
        )


@pytest.fixture
def ingredient_2():
    return Ingredient.objects.create(
        name='Ингредиент_2', 
        measurement_unit='measurement_unit_2'
        )

@pytest.fixture
def tag_1():
    return Tag.objects.create(
        name='Тег_1', 
        color='#FF0000',
        slug='slug_1'
        )

@pytest.fixture
def tag_2():
    return Tag.objects.create(
        name='Тег_2', 
        color='#FF0001',
        slug='slug_2'
        )


@pytest.fixture()
def mock_media(settings):
    with tempfile.TemporaryDirectory() as temp_directory:
        settings.MEDIA_ROOT = temp_directory
        yield temp_directory


# @pytest.fixture
# def recipe(user, ingredient_1, ingredient_2, tag_1):
#     return Recipe.objects.create(
#         name='Название рецепта 1', 
#         text='Описание рецепта 1',
#         author=user, 
#         ingredients=[ingredient_1.get('id'), ingredient_2.get('id')],
#         tags=[tag_1['id'], tag_2['id']],
#         cooking_time=5,
#         image=tempfile.NamedTemporaryFile(suffix=".jpg").name
#     )


# @pytest.fixture
# def post_2(user, group_1):
#     return Post.objects.create(
#         text='Тестовый пост 12342341', author=user, group=group_1
#     )


# @pytest.fixture
# def comment_1_post(post, user):
#     return Comment.objects.create(author=user, post=post, text='Коммент 1')


# @pytest.fixture
# def comment_2_post(post, another_user):
#     return Comment.objects.create(
#         author=another_user, post=post, text='Коммент 2'
#     )


# @pytest.fixture
# def another_post(another_user, group_2):
#     return Post.objects.create(
#         text='Тестовый пост 2', author=another_user, group=group_2
#     )


# @pytest.fixture
# def comment_1_another_post(another_post, user):
#     return Comment.objects.create(
#         author=user, post=another_post, text='Коммент 12'
#     )


# @pytest.fixture
# def follow_1(user, another_user):
#     return Follow.objects.create(user=user, following=another_user)


# @pytest.fixture
# def follow_2(user_2, user):
#     return Follow.objects.create(user=user_2, following=user)


# @pytest.fixture
# def follow_3(user_2, another_user):
#     return Follow.objects.create(user=user_2, following=another_user)


# @pytest.fixture
# def follow_4(another_user, user):
#     return Follow.objects.create(user=another_user, following=user)


# @pytest.fixture
# def follow_5(user_2, user):
#     return Follow.objects.create(user=user, following=user_2)