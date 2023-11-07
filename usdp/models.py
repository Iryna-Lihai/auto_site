from django.db import models



# Create your models here.


class Photo(models.Model):
    image = models.ImageField(upload_to='uploads/usdp/')
    description = models.CharField(max_length=50)

    def __str__(self):
        return self.description

    class Meta:
        verbose_name = "Зображення"
        verbose_name_plural = "Зображення"


class OurCar (models.Model):
    title = models.CharField(max_length=30, verbose_name="Марка і модель")
    year = models.IntegerField(verbose_name="Рік")
    auction_price = models.CharField(verbose_name="Ціна аукціону", max_length=15, default="0")
    final_price = models.CharField(verbose_name="Фінальна ціна",max_length=15,  default="0")
    image = models.ManyToManyField(Photo, blank=True, verbose_name="Зображення")
    url = models.CharField(max_length=200, verbose_name="URL", default="https://www.copart.com")
    main_damage = models.CharField(verbose_name="Основне ушкодження",max_length=15,  default="Front End")
    secondary_damage = models.CharField(verbose_name="Другорядне ушкодження",max_length=50,  default="Minor Dent/Scratches")
    drive = models.CharField(verbose_name="Привід",max_length=30,  default="All Wheel Drive")
    fuel = models.CharField(verbose_name="Паливо", max_length=15, default="Бензин")
    engine = models.CharField(verbose_name="Двигун", max_length=15, default="0")
    mileage = models.CharField(verbose_name="Пробіг", max_length=15, default='100000')



    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Автомобіль"
        verbose_name_plural = "Автомобілі"


class Type(models.Model):
    name = models.CharField(max_length=30, verbose_name="Тип")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Тип"
        verbose_name_plural = "Типи"


class Price(models.Model):
    name = models.CharField(max_length=30,verbose_name="Бюджет авто")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Бюджет авто"
        verbose_name_plural = "Бюджети авто"


class Modals (models.Model):
    type = models.ForeignKey(Type, on_delete=models.CASCADE, default="Седан")
    price = models.ForeignKey(Price, on_delete=models.CASCADE, default="5000$")
    phone = models.CharField(max_length=15, verbose_name="Телефон",  default="+380")

    def __str__(self):
        return self.phone

    class Meta:
        verbose_name = "Вспливаюча форма"
        verbose_name_plural = "Вспливаючі форми"

class SaleLocationCopard(models.Model):
    name = models.CharField(max_length=30,verbose_name="Місце продажу")
    shipping_USA = models.IntegerField(verbose_name="Доставка по США", default=225)
    shipping_ocean = models.IntegerField(verbose_name="Доставка по США", default=1000)


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Місце продажу Copard"
        verbose_name_plural = "Місця продажу Copard"


class SaleLocationIAAI(models.Model):
    name = models.CharField(max_length=30,verbose_name="Місце продажу")
    shipping_USA = models.IntegerField(verbose_name="Доставка по США", default=225)
    shipping_ocean = models.IntegerField(verbose_name="Доставка по США", default=1000)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Місце продажу IAAI"
        verbose_name_plural = "Місця продажу IAAI"
