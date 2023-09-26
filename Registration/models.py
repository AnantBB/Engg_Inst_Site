from django.db import models

# Create your models here.
class person_info(models.Model):
        academic_year = models.CharField(max_length=8)
        course = models.CharField(max_length=20)
        division = models.CharField(max_length=20)
        group = models.CharField(max_length=12)
        arcadian = models.CharField(max_length=4, default=None)
        fname = models.CharField(max_length=12)
        mname = models.CharField(max_length=12)
        lname = models.CharField(max_length=15)
        mother_name = models.CharField(max_length=12)    
        inst_code = models.CharField(max_length=15)
        mobile = models.CharField(max_length=12)
        whatsapp = models.CharField(max_length=12)
        email = models.EmailField(max_length = 30)
    
        def __str__(self):
            return f"{self.fname} {self.lname} has {self.group} as a department"