import sys
from os.path import abspath, dirname, join
import pytest
from django.conf import settings
from dotenv import load_dotenv
import os

load_dotenv()

root_dir = dirname(dirname(abspath(__file__)))
sys.path.append(root_dir)
infra_dir_path = join(root_dir, 'infra')

pytest_plugins = [
    'tests.fixtures.fixture_user',
    'tests.fixtures.fixture_data',
]


# import pytest

# @pytest.mark.django_db
# def test_my_user():
#     me = User.objects.get(username='me')
#     assert me.is_superuser



@pytest.fixture(scope='session')
def django_db_setup():
    settings.DATABASES['default'] = {
        'ENGINE': os.getenv('DB_ENGINE', default='django.db.backends.postgresql'),
        'HOST': os.getenv('DB_PORT', default='5432'),
        'NAME': os.getenv('POSTGRES_DB', default='foodgram'),
        'USER': os.getenv('POSTGRES_USER', default='foodgram_user'),
        'PASSWORD': os.getenv('POSTGRES_PASSWORD', default='1234'),
        'PORT': os.getenv('DB_PORT', default='5432'),
        'ATOMIC_REQUESTS': True,
    }

# from django.core.management import call_command




# @pytest.fixture(scope='session')
# def django_db_setup(django_db_setup, django_db_blocker):
#     with django_db_blocker.unblock():
#         call_command('loaddata', 'my_fixture.json')

