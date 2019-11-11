from django.test import TestCase
from .models import Editor,tags,Category,Location

# Create your tests here.
# Create your tests here.
class EditorTestClass(TestCase):
    def setUp(self):
        self.killa=  Editor(first_name = 'machel', last_name ='killa', email ='killa@gmail.com')
        
    def test_instance(self):
        self.assertTrue(isinstance(self.killa,Editor))
        
    def test_save_method(self):
        self.killa.save_editor()
        editors = Editor.objects.all()
        self.assertTrue(len(editors) > 0)
        
class tagsTestClass(TestCase):
    def setUp(self):
        self.world= tags(name='world')
        
    def test_instance(self):
        self.assertTrue(isinstance(self.world,tags))
        
class LocationTestClass(TestCase):
    def setUp(self):
        self.London= Location(name='London')
        
    def test_instance(self):
        self.assertTrue(isinstance(self.London,Location))
        
    def test_save_method(self):
        self.London.save_location()
        locations = Location.objects.all()
        self.assertTrue(len(locations) > 0)
        
        
class CategoryTestClass(TestCase):
    def setUp(self):
        self.culture= Category(name='cool')
        
    def test_instance(self):
        self.assertTrue(isinstance(self.culture,Category))
        
    def test_save_method(self):
        self.culture.save_category()
        categories = Category.objects.all()
        self.assertTrue(len(categories) > 0)
        