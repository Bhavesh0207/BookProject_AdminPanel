from django.contrib import admin
from .models import category, bookinfo, author, country, state, city
# Register your models here.
class showcategory(admin.ModelAdmin):
    list_display = ["cat_name"]

admin.site.register(category, showcategory)

class showbookinfo(admin.ModelAdmin):
    list_display = ["b_name", "b_info", "b_price", "b_quantity", "b_description", "b_pages", "admin_photo", "cat_name"]

admin.site.register(bookinfo, showbookinfo)

class showauthor(admin.ModelAdmin):
    list_display = ["a_name", "a_gender", "a_email", "admin_photo", "a_description"]

admin.site.register(author, showauthor)

class showcountry(admin.ModelAdmin):
    list_display = ["country_name"]

admin.site.register(country,showcountry)

class showstate(admin.ModelAdmin):
    list_display = ["country_name", "state_name"]

admin.site.register(state,showstate)

class showcity(admin.ModelAdmin):
    list_display = ["state_name", "city_name"]

admin.site.register(city,showcity)