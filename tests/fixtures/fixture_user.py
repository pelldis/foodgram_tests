import pytest


@pytest.fixture
def user(django_user_model):
    return django_user_model.objects.create_user(
        email='TestUser1@mail.ru', password='1234567', username='TestUser1'
    )


#@pytest.fixture
#def user_2(django_user_model):
#    return django_user_model.objects.create_user(
#        username='TestUser2', password='1234567'
#    )
#
#
#@pytest.fixture
#def another_user(django_user_model):
#    return django_user_model.objects.create_user(
#        username='TestUserAnother', password='1234567'
#    )
#
#
# @pytest.fixture
# def token(user):
#    from rest_framework_simplejwt.tokens import RefreshToken
#    refresh = RefreshToken.for_user(user)

#    return {
#        'refresh': str(refresh),
#        'access': str(refresh.access_token),
#    }


# @pytest.fixture
# def user_client(token):
#     from rest_framework.test import APIClient

#     client = APIClient()
#     client.credentials(HTTP_AUTHORIZATION=f'Bearer {token["access"]}')
#     return client

@pytest.fixture
def token(user):
    from rest_framework.authtoken.models import Token
    token, _ = Token.objects.get_or_create(user=user)
    return token.key


@pytest.fixture
def user_client(token):
    from rest_framework.test import APIClient

    client = APIClient()
    client.credentials(HTTP_AUTHORIZATION=f'Token {token}')
    return client