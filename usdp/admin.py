from django.contrib import admin
from .models import OurCar, Photo, Modals, Price, Type, SaleLocationCopard, SaleLocationIAAI

# Register your models here.
admin.site.register(OurCar)
admin.site.register(Photo)

admin.site.register(Modals)
admin.site.register(Price)
admin.site.register(Type)
admin.site.register(SaleLocationCopard)
admin.site.register(SaleLocationIAAI)


