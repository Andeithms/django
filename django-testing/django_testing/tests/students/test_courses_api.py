import pytest
import random
from django.urls import reverse
import rest_framework.status as status


@pytest.mark.django_db
def test_single_course(api_client, course_factory, student_factory):
    course = course_factory(students=student_factory())
    index = random.randrange(5)
    url = reverse("courses-detail", args=[course[index].id])
    resp = api_client.get(url)
    resp_json = resp.json()

    assert resp.status_code == status.HTTP_200_OK
    assert resp_json["id"] == course[index].id


@pytest.mark.django_db
def test_list_course(api_client, course_factory, student_factory):
    course_factory(students=student_factory())
    url = reverse("courses-list")
    resp = api_client.get(url)
    resp_json = resp.json()

    assert resp.status_code == status.HTTP_200_OK
    assert len(resp_json) == 5


@pytest.mark.django_db
def test_id_course(api_client, course_factory, student_factory):
    course = course_factory(students=student_factory())
    id = random.choice(course).id
    url = reverse("courses-list")
    resp = api_client.get(url, data={"id": id})
    resp_json = resp.json()

    assert resp.status_code == status.HTTP_200_OK
    assert resp_json[0]['id'] == id


@pytest.mark.django_db
def test_name_course(api_client, course_factory, student_factory):
    course = course_factory(students=student_factory())
    name = random.choice(course).name
    url = reverse("courses-list")
    resp = api_client.get(url, data={"name": name})
    resp_json = resp.json()

    assert resp.status_code == status.HTTP_200_OK
    assert resp_json[0]['name'] == name


@pytest.mark.django_db
def test_create_course(api_client, course_factory, student_factory):
    url = reverse("courses-list")
    resp = api_client.post(url, data={'name': 'added_course'}, format="json")
    resp_json = resp.json()

    assert resp.status_code == status.HTTP_201_CREATED
    assert resp_json['name'] == 'added_course'


@pytest.mark.django_db
def test_update_course(api_client, course_factory, student_factory):
    course = course_factory(students=student_factory())
    index = random.choice(course).id
    url = reverse("courses-detail",  args=[index])
    resp = api_client.patch(url, data={'id': index, 'name': 'update_course'}, format="json")
    resp_json = resp.json()

    assert resp.status_code == status.HTTP_200_OK
    assert resp_json['id'] == index and resp_json['name'] == 'update_course'


@pytest.mark.django_db
def test_delete_course(api_client, course_factory, student_factory):
    course = course_factory(students=student_factory())
    index = random.choice(course).id
    url = reverse("courses-detail",  args=[index])
    resp = api_client.delete(url)
    new_resp = api_client.get(reverse("courses-list"))
    resp_json = new_resp.json()
    list_id = [i['id'] for i in resp_json]

    assert resp.status_code == status.HTTP_204_NO_CONTENT
    assert new_resp.status_code == status.HTTP_200_OK
    assert index not in list_id
