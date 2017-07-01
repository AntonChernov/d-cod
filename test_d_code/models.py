from django.db import models

# Create your models here.


class DataSetModel(models.Model):
    group_region = models.CharField(max_length=100)
    parameter_country = models.CharField(max_length=100)
    value = models.CharField(max_length=10)

    class Meta:
        db_table = 'dataset'
        verbose_name_plural = 'датасеты'

    def __str__(self):
        return self.group_region

    def as_dict(self):
        items = {
            'region': self.group_region,
            'country': self.parameter_country,
            'value': self.value,
        }
        return items