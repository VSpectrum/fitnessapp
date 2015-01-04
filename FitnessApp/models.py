from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class Users(models.Model):
    Gender = (
        ('F', 'Female'),
        ('M', 'Male'),
    )
    UserFirstName = models.CharField(max_length=50, blank=False)
    UserLastName = models.CharField(max_length=50, blank=False)
    UserBday = models.DateField(blank=False)
    UserGender = models.CharField(max_length=1, choices=Gender, blank=False)
    UserEmail = models.EmailField(max_length=50)
    UserPhoneNumber = PhoneNumberField()
    dateTCreated = models.DateTimeField(auto_now_add=True)
    IsTrainer = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Users'
        verbose_name_plural = 'Users'

    def __unicode__(self):
        return self.UserFirstName


class UserDisabilities(models.Model):
    FitnessUser = models.ForeignKey(Users)
    Disability	= models.CharField(max_length=50)

    class Meta:
        verbose_name = 'User Disabilities'
        verbose_name_plural = 'User Disabilities'

    def __unicode__(self):
        return self.FitnessUser.UserFirstName


class Equipment(models.Model):
    ItemName = models.CharField(max_length=80, unique=True, blank=False)
    BoughtPrice = models.DecimalField(max_digits=8, decimal_places=2)
    ContactEmail = models.EmailField(max_length=50)
    ContactPhone = PhoneNumberField()

    class Meta:
        verbose_name = 'Equipment'
        verbose_name_plural = 'Equipment'

    def __unicode__(self):
        return self.ItemName


class EquipmentUsage(models.Model):
    Equipment = models.ForeignKey(Equipment)
    Usedby = models.ForeignKey(Users)
    TimeUsed = models.TimeField()

    class Meta:
        verbose_name = 'Equipment Usage'
        verbose_name_plural = 'Equipment Usage'

    def __unicode__(self):
        return self.Usedby.UserFirstName


class EquipmentRepairHistory(models.Model):
    EquipmentName = models.ForeignKey(Equipment)
    DateRepaired = models.DateTimeField()

    class Meta:
        verbose_name = 'Equipment Repair History'
        verbose_name_plural = 'Equipment Repair History'

    def __unicode__(self):
        return self.EquipmentName.ItemName


class TrainerTrainee(models.Model):
    Trainer = models.ForeignKey(Users, related_name='Trainer')
    Trainee = models.ForeignKey(Users, related_name='Trainee')

    class Meta:
        verbose_name = 'Trainer Trainee'
        verbose_name_plural = 'Trainer Trainee'

    def __unicode__(self):
        return self.Trainer.UserFirstName
