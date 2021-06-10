from django.db import models

# Create your models here.

class Leads(models.Model):

    customer_name = models.CharField(max_length=50)
    customer_email = models.EmailField()
    customer_phone = models.IntegerField()
    customer_zip = models.IntegerField()
    date_created = models.DateTimeField(auto_now=True)
    part = models.CharField(max_length=50)
    make_model = models.CharField(max_length=100)
    year = models.IntegerField()

    def __str__(self):
        return self.customer_name
