from django.test import TestCase
from django.urls import reverse
from .models import Contact

class ContactsViewTests(TestCase):
    def setUp(self):
        # Create a sample contact for testing
        self.contact = Contact.objects.create(
            name='John Doe',
            email='john.doe@example.com',
            phone='1234567890'
        )

    def test_contact_list_view(self):
        response = self.client.get(reverse('contact_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contacts/contact_list.html')

    def test_add_contact_view(self):
        response = self.client.get(reverse('add_contact'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contacts/add_contact.html')

    def test_edit_contact_view(self):
        response = self.client.get(reverse('edit_contact', args=[self.contact.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contacts/edit_contact.html')

    def test_delete_contact_view(self):
        response = self.client.get(reverse('delete_contact', args=[self.contact.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contacts/delete_contact.html')
