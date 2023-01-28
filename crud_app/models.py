from django.db import models


class Staff(models.Model):
    name = models.CharField('ФИО сотрудника', max_length=80)
    department = models.ForeignKey(to='SelectDep', on_delete=models.CASCADE)
    register_date = models.DateTimeField('Дата и время создания записи', null=True, blank=True, default=None)

    def __str__(self):
        return self.name

class SelectDep(models.Model):
    name_department = models.CharField(max_length=50)

    def __str__(self):
        return self.name_department