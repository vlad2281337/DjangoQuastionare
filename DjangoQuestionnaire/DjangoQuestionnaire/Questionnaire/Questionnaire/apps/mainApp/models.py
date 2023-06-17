from django.db import models
from django.contrib.auth.models import AbstractUser

ROLES = (
    (1, 'Лікар'),
    (2, 'Пацієнт')
)


class User(AbstractUser):
    role = models.PositiveSmallIntegerField(choices=ROLES, default=1)

    def __str__(self):
        return self.get_full_name() + ' (' + self.get_username() + ') ' + str(dict(ROLES)[self.role])


class Doctor(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Користувач')
    specialization = models.TextField('Спеціалізація')

    def __str__(self):
        return self.user.get_full_name() + ' / ' + self.specialization

    class Meta:
        verbose_name = 'Лікар'
        verbose_name_plural = 'Лікарі'


class Appointment(models.Model):
    id = models.AutoField(primary_key=True)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, verbose_name='Лікар')
    patietn = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пацієнт')
    date = models.DateField(verbose_name='Дата прийому')
    time = models.TimeField(verbose_name='Час прийому')
    complains = models.TextField('Причини звернення')
    symptoms = models.TextField('Симптоматика', blank=True, null=True)
    diagnosys = models.TextField('Діагноз', blank=True, null=True)
    recomendations = models.TextField('Рекомендації', blank=True, null=True)

    def __str__(self):
        return self.doctor.user.get_full_name() + ' (' + self.doctor.specialization + ') ' +' / ' + self.patietn.get_full_name() + ' ' \
               + str(self.date) + ' ' + str(self.time)

    class Meta:
        verbose_name = 'Прийом'
        verbose_name_plural = 'Прийоми'
        ordering = ('diagnosys',)



class Medical(models.Model):
    name = models.TextField('Назва')
    description = models.TextField('Опис')
    reception = models.BooleanField('Рецептурний препарат')

    def __str__(self):
        return self.name


    class Meta:
        verbose_name = 'Ліки'
        verbose_name_plural = 'Ліки'





class Orders(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Замовник')
    medical = models.ForeignKey(Medical, on_delete=models.CASCADE, verbose_name='Ліки')


    def __str__(self):
        return self.user.get_full_name() + ' — ' +  self.medical.name

    class Meta:
        verbose_name = 'Замовлення'
        verbose_name_plural = 'Замовлення'
