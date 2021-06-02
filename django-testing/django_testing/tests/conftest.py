import pytest
from rest_framework.test import APIClient
from model_bakery import baker


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def student_factory():
    def func(**kwargs):
        return baker.make("Student", _quantity=20, **kwargs)

    return func


@pytest.fixture
def course_factory():
    def func(**kwargs):
        return baker.make("Course", _quantity=5, **kwargs)

    return func
