from django.db import models
from django.utils.safestring import mark_safe

VEL = (
    ("FICTION", "FICTION"),
    ("METHOLOGY", "METHOLOGY"),
    ("HORROR", "HORROR"),
    ("STUDY", "STUDY"),
    ("UPSC", "UPSC"),
)

GEN = (
    ("MALE", "MALE"),
    ("FEMALE", "FEMALE")
)
# Create your models here.
class category(models.Model):
    cat_name = models.CharField(max_length=20, choices=VEL)

    def __str__(self):
        return self.cat_name

class bookinfo(models.Model):
    b_name = models.CharField(max_length=20)
    b_info = models.TextField()
    b_price = models.IntegerField()
    b_quantity = models.IntegerField()
    b_description = models.TextField()
    b_pages = models.IntegerField()
    b_image = models.ImageField(upload_to="photos")
    cat_name = models.ForeignKey(category, on_delete=models.CASCADE)

    def __str__(self):
        return self.b_name

    def admin_photo(self):
        return mark_safe('<img src="{}" width="100"/>'.format(self.b_image.url))

    admin_photo.allow_tags = True


class author(models.Model):
    a_name = models.CharField(max_length=20)
    a_gender = models.CharField(max_length=20, choices=GEN)
    a_email = models.EmailField()
    a_profilepic = models.ImageField(upload_to="photos")
    a_description = models.TextField()

    def __str__(self):
        return self.a_name

    def admin_photo(self):
        return mark_safe('<img src="{}" width="100"/>'.format(self.a_profilepic.url))

    admin_photo.allow_tags = True


class country(models.Model):
    country_name = models.CharField(max_length=20)

    def __str__(self):
        return self.country_name

class state(models.Model):
    country_name = models.ForeignKey(country, on_delete=models.CASCADE)
    state_name = models.CharField(max_length=20)

    def __str__(self):
        return self.state_name

class city(models.Model):
    state_name = models.ForeignKey(state, on_delete=models.CASCADE)
    city_name = models.CharField(max_length=20)

    def __str__(self):
        return self.city_name