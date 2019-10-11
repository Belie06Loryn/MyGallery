from django.db import models
import datetime as dt

class Category(models.Model):
    cate = models.CharField(max_length =30)

    def save_cate(self):
        self.save()

    def dele_cate(self):
        self.delete() 

    def __str__(self):
        return self.cate       

class Location(models.Model):
    location = models.CharField(max_length =30)

    def save_loca(self):
        self.save()

    def dele_loca(self):
        self.delete()    

    def __str__(self):
        return self.location

class Photos(models.Model):
    image = models.ImageField(upload_to = 'photos/',null=True)
    name = models.CharField(max_length =40)
    descri = models.TextField(max_length =6000)
    pub_date = models.DateTimeField(auto_now_add=True)
    cate = models.ForeignKey(Category)
    loca = models.ForeignKey(Location ,null=True)
     
    
    def save_pic(self):
        self.save()
                      
    @classmethod
    def search_by_cate(cls,search):
        categories = cls.objects.filter(cate__cate__icontains=search)
        return categories  

    def dele_pic(self):
        self.delete() 

    @classmethod
    def image_by_id(cls,id):
        found = cls.objects.filter(pk = id)
        return found
    

    @classmethod
    def filter_loca(cls,location):
        imaje = cls.objects.filter(location__location__icontains=location)
        return imaje

    @classmethod
    def update_pic(cls,id):
        imaje = cls.objects.filter(id=id).update(id=id)
        return imaje

    def __str__(self):
        return self.name                 