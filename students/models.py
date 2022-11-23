from django.db import models


# Create your models here.

class GenderTypeChoices(models.TextChoices):
    male = 'Male'
    female = 'Female'
    other = 'Other'


class Student(models.Model):
    # GENDER_TYPE = (
    #     ('male', 'Male'),
    #     ('female', 'Female')
    # )

    course = models.ForeignKey('students.Course', on_delete=models.SET_NULL, null=True, verbose_name='Курс')

    first_name = models.CharField(max_length=50, null=True, verbose_name='Имя')
    last_name = models.CharField(max_length=50, verbose_name='Фамилия')
    birth_date = models.DateField(null=True)
    # gender = models.CharField(choices=GENDER_TYPE)
    gender = models.CharField(max_length=7, choices=GenderTypeChoices.choices, default=GenderTypeChoices.male)
    email = models.EmailField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.full_name

    @property
    def full_name(self) -> str:
        return f'{self.first_name} {self.last_name}'

    class Meta:
        ordering = ['-created_at']
        verbose_name_plural = 'Ученики'
        # constraints = [
        #     models.CheckConstraint(
        #         verbose_name_plural=''
        #     )
        # ]


class Course(models.Model):
    name = models.CharField(max_length=150, verbose_name='Название курса')

    class Meta:
        verbose_name_plural = 'Курсы'

    def __str__(self):
        return self.name