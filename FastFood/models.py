from django.db import models
from django.utils.translation import gettext_lazy as _


class CommonInfo(models.Model):
    city = models.CharField(max_length=200, verbose_name=_("city"))
    street = models.CharField(max_length=200, verbose_name=_("street"))
    number = models.IntegerField(verbose_name=_("number"))
    lat = models.FloatField()
    long = models.FloatField()


class Client(models.Model):
    name = models.CharField(max_length=200, verbose_name=_("name"))
    iban = models.IntegerField()
    bank = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = _("Clients")


class Customer(models.Model):
    name = models.CharField(max_length=200, verbose_name=_("name"))
    email = models.EmailField()
    phone = models.IntegerField(verbose_name=_("phone"))

    class Meta:
        verbose_name = _("Customer")
        verbose_name_plural = _("Customers")


class Address(CommonInfo):
    block = models.CharField(max_length=200, blank=True, verbose_name=_("block"))
    stair = models.IntegerField(blank=True, verbose_name=_("stair"))
    room = models.IntegerField(blank=True, verbose_name=_("room"))
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name="addresses")

    class Meta:
        verbose_name = _("Address")
        verbose_name_plural = _("Addresses")


class Category(models.Model):
    name = models.CharField(max_length=200, verbose_name=_("name"))

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")


class Product(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name="products")
    category = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL, related_name="products")
    name = models.CharField(max_length=200,  verbose_name=_("name"))
    price = models.DecimalField(max_digits=5, decimal_places=2, verbose_name=_("price"))
    content = models.CharField(max_length=200, verbose_name=_("content"))

    class Meta:
        verbose_name = _("Product")
        verbose_name_plural = _("Products")


class DailyMenu(models.Model):
    date = models.DateTimeField(verbose_name=_("date"))
    product = models.ManyToManyField(Product, related_name="daily_menus")

    class Meta:
        verbose_name = _("DailyMenu")


class Location(CommonInfo):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name="locations")

    class Meta:
        verbose_name = _("Location")
        verbose_name_plural = _("Locations")


class Menu(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name="menus")
    product = models.ManyToManyField(Product, related_name="products_list")
    category = models.ManyToManyField(Category, related_name="categories_list")
    price = models.DecimalField(max_digits=5, decimal_places=2, verbose_name=_("price"))

    class Meta:
        verbose_name = _("Menu")
        verbose_name_plural = _("Menus")


class OrderBillingDetails(models.Model):
    article = models.CharField(max_length=200, verbose_name=_("article"))
    number_of_items = models.IntegerField(verbose_name=_("number_of_items"))
    price_per_item = models.DecimalField(max_digits=5, decimal_places=2, verbose_name=_("price_per_piece"))

    class Meta:
        verbose_name = _("OrderBillingDetails")


class Order(models.Model):
    date = models.DateTimeField(verbose_name=_("date"))
    customer = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL, related_name="orders")
    total_price = models.DecimalField(max_digits=5, decimal_places=2, verbose_name=_("total_price"))
    paid = models.BooleanField(verbose_name=_("paid"))


class OrderProductDetails(models.Model):
    product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL, related_name="orders")
    order = models.ForeignKey(Order, null=True, on_delete=models.SET_NULL, related_name="order_details")
    number_of_items = models.IntegerField(verbose_name=_("number_of_items"))
    price = models.DecimalField(max_digits=5, decimal_places=2, verbose_name=_("price_per_piece"))
