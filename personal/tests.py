from django.test import TestCase
from .models import Location,Photos,Category
 import datetime as dt
 
class LocationTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.ahantu= Location(location = 'Rwanda')

    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.ahantu,Location))    

    # Testing Save Method
    def test_save_method(self):
        self.ahantu.save_loca()
        locations = Location.objects.all()
        self.assertTrue(len(locations) > 0)   

class CategoryTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.categ= Category(category = 'Fun')

    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.categ,Category))    

    # Testing Save Method
    def test_save_method(self):
        self.categ.save_cate()
        categories = Category.objects.all()
        self.assertTrue(len(categories) > 0)          

class PhotosTestClass(TestCase):

    def setUp(self):
        # Creating a new Location and saving it
        self.ahantu= Location(location='Rwanda')
        self.ahantu.save_location()

        # Creating a new category and saving it
        self.new_cate = Category(name = 'Fun')
        self.new_cate.save_cate()

        self.new_photos= Photos(image = 'Jam.jpeg', name ='Muriuki', descri ='jamesmoringaschoolcom',loca = self.location, cate=self.category,pub_date = '2019-09-29')
        self.new_photos.save_pic()

        self.new_photos.Category.add(self.new_cate)

    def tearDown(self):
        Location.objects.all().delete()
        Category.objects.all().delete()
        Photos.objects.all().delete()       

        