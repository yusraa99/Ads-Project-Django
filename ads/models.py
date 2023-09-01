from django.db import models
from django.contrib.auth.models import User

# Create your models here.
    # - title
    # - Location
    # - Image
    # - Price
    # - Description
    # - Published at
    # - User_name
    # - category


def image_upload(instance,filename):
    imagename , extenstion = filename.split(".")
    return "adsimage/%s.%s"%(instance.id,extenstion)


# [ "Jobs", "Purchases", "Selling"]
CATEGORY = (
    ('Jobs','Jobs'),
    ('Purchases','Purchases'),
    ('Selling','Selling'),
)


class Ads(models.Model):
    
    title= models.CharField(max_length=50)
    location= models.CharField(max_length=100)
    image=models.ImageField(upload_to=image_upload)
    price = models.IntegerField(default=0)
    description= models.TextField(max_length=1000)
    published_at=models.DateTimeField(auto_now=True)
    category=models.CharField(max_length=15, choices=CATEGORY)
    user= models.ForeignKey(User, on_delete=models.CASCADE,blank=True, null=True)

    def __str__(self):
        return self.title
    
    def title_url(self):
        return self.title.replace(' ','-')

