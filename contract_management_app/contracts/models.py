from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Contract(models.Model):
    contract_type_choices = [
        ('service', 'Service'),
        ('goods', 'Goods')
    ]
    currency_choices = [
        ('RUR', 'Russian Ruble'),
        ('EUR', 'Euro'),
        ('USD', 'USA Dollar')
    ]
    title = models.CharField(max_length=100)
    date_created = models.DateTimeField(default=timezone.now)
    # date_last_modified =
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    contract_type = models.CharField(max_length=7, choices=contract_type_choices, default='goods')  # service or goods
    contract_currency = models.CharField(max_length=3, choices=currency_choices, default='RUR')
    contract_amount = models.DecimalField(default=0, max_digits=15, decimal_places=2)
    contract_file = models.FileField(upload_to='contracts')
    contract_specification = models.FileField(upload_to='contracts', null=True, blank=True)
    contract_appendix1 = models.FileField(upload_to='contracts', null=True, blank=True)
    contract_appendix2 = models.FileField(upload_to='contracts', null=True, blank=True)
    contract_file_signed = models.FileField(upload_to='contracts/signed', null=True, blank=True)

    def __str__(self):
        return self.title
