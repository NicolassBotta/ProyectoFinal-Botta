from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from .models import libro, revista


class SeguridadVistasTests(TestCase):
    def setUp(self):
        self.owner = User.objects.create_user(username="owner", password="pass12345")
        self.other = User.objects.create_user(username="other", password="pass12345")

        self.libro = libro.objects.create(
            nombre="Libro A",
            autor="Autor A",
            usuario=self.owner,
            telefono_del_duenio="1111111111",
        )
        self.revista = revista.objects.create(
            editorial="Editorial A",
            titulo="Revista A",
            usuario=self.owner,
            telefono_del_duenio="2222222222",
        )

    def test_editarperfil_requiere_login(self):
        response = self.client.get(reverse("editaperfil"))
        self.assertEqual(response.status_code, 302)
        self.assertIn(reverse("login"), response.url)

    def test_agregar_avatar_requiere_login(self):
        response = self.client.get(reverse("agregar_avatar"))
        self.assertEqual(response.status_code, 302)
        self.assertIn(reverse("login"), response.url)

    def test_no_autor_no_puede_editar_libro(self):
        self.client.login(username="other", password="pass12345")
        response = self.client.get(reverse("EditarLibro", args=[self.libro.pk]))
        self.assertEqual(response.status_code, 403)

    def test_no_autor_no_puede_borrar_libro(self):
        self.client.login(username="other", password="pass12345")
        response = self.client.get(reverse("BorrarLibro", args=[self.libro.pk]))
        self.assertEqual(response.status_code, 403)

    def test_no_autor_no_puede_editar_revista(self):
        self.client.login(username="other", password="pass12345")
        response = self.client.get(reverse("EditarRevista", args=[self.revista.pk]))
        self.assertEqual(response.status_code, 403)

    def test_no_autor_no_puede_borrar_revista(self):
        self.client.login(username="other", password="pass12345")
        response = self.client.get(reverse("BorrarRevista", args=[self.revista.pk]))
        self.assertEqual(response.status_code, 403)
