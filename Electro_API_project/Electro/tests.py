from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APITestCase

from .models import Electro


class ElectroModelTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        test_user = get_user_model().objects.create_user(
            username="tester", password="pass"
        )
        test_user.save()

        test_electro_content = Electro.objects.create(
            owner=test_user,
            elctronic_name="name of electro",
            description="Words about the electro",
        )
        test_electro_content.save()

    def test_Electro_content(self):
        electro = Electro.objects.get(id=1)

        self.assertEqual(str(electro.owner), "tester")
        self.assertEqual(electro.elctronic_name, "name of electro")
        self.assertEqual(electro.description, "Words about the electro")


class APITest(APITestCase):
    def test_list(self):
        response = self.client.get(reverse("electro_list"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_detail(self):

        test_user = get_user_model().objects.create_user(
            username="tester", password="pass"
        )
        test_user.save()

        test_electro_content = Electro.objects.create(
            owner=test_user,
            elctronic_name="name of electro",
            description="Words about the electro",
        )
        test_electro_content.save()

        response = self.client.get(reverse("electro_detail", args=[1]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.get("id"), 1)
        self.assertEqual(response.data.get("owner"), test_electro_content.id)
        self.assertEqual(
            response.data.get("elctronic_name"), test_electro_content.elctronic_name
        )
        self.assertEqual(
            response.data.get("description"), test_electro_content.description
        )

    def test_create(self):
        test_user = get_user_model().objects.create_user(
            username="tester", password="pass"
        )
        test_user.save()

        url = reverse("electro_list")
        data = {
            "elctronic_name": "Testing is Fun!!!",
            "description": "when the right tools are available",
            "owner": test_user.id,
        }

        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED, test_user.id)
        self.assertEqual(Electro.objects.count(), 1)
        self.assertEqual(Electro.objects.get().elctronic_name, data["elctronic_name"])

    def test_update(self):
        test_user = get_user_model().objects.create_user(
            username="tester", password="pass"
        )
        test_user.save()

        test_electro_content = Electro.objects.create(
            owner=test_user,
            elctronic_name="name of electro",
            description="Words about the electro",
        )

        test_electro_content.save()

        url = reverse("electro_detail", args=[1])
        data = {
            "electro_name": "Testing is Still Fun!!!",
            "owner": test_electro_content.owner.id,
            "description": "Words about the electro",
        }
        
        response = self.client.put(url, data, format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK, url)

        self.assertEqual(Electro.objects.count(), test_electro_content.id)
        self.assertEqual(Electro.objects.get().elctronic_name, data["electro_name"])


    def test_delete(self):
        """Test the api can delete a post."""

        test_user = get_user_model().objects.create_user(username='tester',password='pass')
        test_user.save()

        test_electro_content = Electro.objects.create(
            owner = test_user,
            elctronic_name = 'Title of electro',
            description = 'Words about the electro'
        )

        test_electro_content.save()

        electro = Electro.objects.get()

        url = reverse('electro_detail', kwargs={'pk': electro.id})


        response = self.client.delete(url)

        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT, url)
