import datetime

from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _

STATUS_TYPES = (('X', _('In progress')), ('A', _('Repaid')), ('C', _('Cancel')))


class Category(models.Model):
    category_name = models.CharField(max_length=200)

    def __str__(self):
        return self.category_name


class Debt(models.Model):
    creditor = models.ForeignKey(settings.AUTH_USER_MODEL,
                                 related_name='users_who_give_loan',
                                 on_delete=models.CASCADE,
                                 verbose_name=_('Creditor'))
    debtor = models.ForeignKey(settings.AUTH_USER_MODEL,
                               related_name='users_who_get_money',
                               on_delete=models.CASCADE,
                               verbose_name=_('Debtor'))
    item_name = models.CharField(max_length=200)
    category = models.ForeignKey(Category, related_name='category', verbose_name=_('Category'))
    amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_('Amount'))
    status = models.CharField(max_length=1, choices=STATUS_TYPES, default='X', verbose_name=_('Status'))
    create_date = models.DateField(default=datetime.date.today, verbose_name=_('Date'))
