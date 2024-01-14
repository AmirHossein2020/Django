from django.db import models
from django.utils.translation import gettext as _
# Create your models here.

class Reservation(models.Model):
    name = models.CharField(_("نام و نام خانوادگی"),max_length=500)
    emali = models.EmailField(_("ادرس الکترونیکی"),max_length=500)
    phone = models.CharField(_("تلفن"),max_length=500)
    number = models.IntegerField(_("تعداد"))
    date = models.DateField(_("تاریخ"), auto_now=False, auto_now_add=False)
    time = models.TimeField(_("ساعت"), auto_now=False, auto_now_add=False)
    

    def __str__(self):
        return self.emali
    

