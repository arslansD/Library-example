from django.test import TestCase
from django.urls import reverse

from .models import Book

class BookTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.book = Book.objects.create(
            title='Test Title',
            subtitle='Test Subtitle',
            author='Test Author',
            isbn='123123234',
        )

    def test_book_content(self):
        self.assertEqual(self.book.title, 'Test Title')
        self.assertEqual(self.book.subtitle, 'Test Subtitle')
        self.assertEqual(self.book.author, 'Test Author')
        self.assertEqual(self.book.isbn, '123123234')

    def test_book_listview(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Title')
        self.assertTemplateUsed(response, 'books/book_list.html')