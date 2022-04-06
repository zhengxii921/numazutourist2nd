from django.test import TestCase
from django.urls import reverse, resolve
from ..views import IndexView, LovenumaListView

# Create your tests here.

class TestUrls(TestCase):


    def test_index_url(self):
        view = resolve("/numazutourist/")
        self.assertEqual(view.func.view_class, IndexView)

    
    def test_lovenuma_list_url(self):
        view = resolve("/numazutourist/lovenumazu")
        self.assertEqual(view.func.view_class, LovenumaListView)
