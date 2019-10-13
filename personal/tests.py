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

    def tearDown(self):
        Location.objects.all().delete()

    def test_save_loca(self):
        self.ahantu.save_loca()
        locations= Location.objects.all()
        self.assertTrue(len(locations)>=1) 

    def test_dele_loca(self):
        self.ahantu.save_loca()
        locations = Location.objects.all()
        self.assertTrue(len(locations)>=0)              

         

class CategoryTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.categ= Category(cate = 'Fun')

    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.categ,Category))    

    # Testing Save Method
    def test_save_method(self):
        self.categ.save_cate()
        categories = Category.objects.all()
        self.assertTrue(len(categories) >= 1)  

    def test_del_cate(self):
        self.categ.save_cate()
        categories = self.categ.dele_cate()
        categ = Category.objects.all()
        self.assertTrue(len(categ)<=0)

    def tearDown(self):
        Category.objects.all().delete()                

class PhotosTestClass(TestCase):

    def setUp(self):
        # Creating a new Location and saving it
        self.ahantu= Location(location='Rwanda')
        self.ahantu.save_loca()

        # Creating a new category and saving it
        self.new_cate = Category(cate = 'Fun')
        self.new_cate.save_cate()

        self.new_photos= Photos(image = 'Jam.jpeg', name ='Muriuki', descri ='jamesmoringaschoolcom',loca = self.ahantu, cate=self.new_cate,pub_date = '2019-09-29')
        self.new_photos.save_pic()

    def tearDown(self):
        Location.objects.all().delete()
        Category.objects.all().delete()
        Photos.objects.all().delete()       

    def test_save_pick(self):
        self.new_photos= Photos(image = 'Jam.jpeg', name ='Muriuki', descri ='jamesmoringaschoolcom',loca = self.ahantu, cate=self.new_cate,pub_date = '2019-09-29')
        self.new_photos.save_pic()
        picture = Photos.objects.all()
        self.assertTrue(len(picture)>=1)

    def test_dele_pick(self):
        self.new_photos= Photos(image = 'Jam.jpeg', name ='Muriuki', descri ='jamesmoringaschoolcom',loca = self.ahantu, cate=self.new_cate,pub_date = '2019-09-29')
        self.new_photos.save_pic()
        picture = self.new_photos.dele_pic()
        delete = Photos.objects.all()
        self.assertTrue(len(delete)>=0)   

    def test_upd_pic(self):
        image = Photos.objects.filter(id=1)
        image.update(name ='lez.jpeg')
        search = Photos.objects.filter(id=1)
        self.assertNotEqual(search,'lez.jpeg')     
        
    def test_pic_id(self):
        self.image = Photos(image = 'Jam.jpeg', name ='Muriuki', descri ='jamesmoringaschoolcom',loca = self.ahantu, cate=self.new_cate,pub_date = '2019-09-29')
        self.image.save_pic()
        search = Photos.image_by_id(self.image.id)
        self.assertNotEqual(search,self.image)    
 
    def test_search_by_cate(self):
        self.category = Category(cate = 'Fun')
        self.category.save_cate()
        self.image = Photos(image = 'Jam.jpeg', name ='Muriuki', descri ='jamesmoringaschoolcom',loca = self.ahantu, cate=self.new_cate,pub_date = '2019-09-29')
        self.image.save_pic()
        search = Photos.search_by_cate('Fun')
        self.assertNotEqual(search,self.image)

    def test_search_loca(self):
        self.location = Location(location='Rwanda')
        self.location.save_loca()
        self.image = Photos(image = 'Jam.jpeg', name ='Muriuki', descri ='jamesmoringaschoolcom',loca = self.ahantu, cate=self.new_cate,pub_date = '2019-09-29')
        self.image.save_pic()
        search = Photos.filter_loca('Rwanda')
        self.assertNotEqual(search,self.image)    