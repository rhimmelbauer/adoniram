
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):

    SX_ADMIN = 1
    SX_MANAGER = 2
    SX_CONTRATOR = 3

    USER_TYPES = ((SX_ADMIN, "Admin"),
                  (SX_MANAGER, "Manager"),
                  (SX_CONTRATOR, "Contractor")
    )
    username = None
    iduser = models.AutoField(primary_key=True)
    name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=150)
    passwords = models.CharField(max_length=150)
    user_type = models.IntegerField('User Type', choices=USER_TYPES, default=SX_CONTRATOR)
    rate = models.DecimalField(max_digits=5, decimal_places=2)
    USERNAME_FIELD = 'iduser'

    class Meta:
        db_table = 'user'

    def __repr__(self):
        return f"\nID:{self.iduser}\n" + \
               f"Name:{self.name}\n" + \
               f"Last Name:{self.last_name}\n" + \
               f"email:{self.email}\n" + \
               f"Type:{self.user_type}\n" + \
               f"Rate per Hour:{self.rate}\n"

class Group(models.Model):
    id_user_mentor = models.IntegerField(primary_key=True)
    id_user_contractor = models.IntegerField()

    class Meta:
        db_table = 'group'

class Work(models.Model):
    
    OTHER = 0
    CONTENT_CREATION = 1
    WEBINAR = 2
    FINANCE = 3
    MANAGEING = 4
    WORK_TYPE = (
        (CONTENT_CREATION, "Content Creation"),
        (WEBINAR, "Webinar"),
        (FINANCE, "Finance"),
        (MANAGEING, "Manageing"),
        (OTHER, "Other")
    )

    idwork = models.AutoField(primary_key=True)
    iduser = models.ForeignKey(User, models.DO_NOTHING, db_column='iduser')
    hours = models.DecimalField(max_digits=5, decimal_places=2)
    work_type = models.CharField(max_length=45)
    month = models.IntegerField(blank=True, default=0)
    notes = models.CharField(max_length=250, blank=True)
    logged_on = models.DateTimeField(auto_now_add=True, blank=True)

    class Meta:
        db_table = 'work'
        unique_together = (('idwork', 'iduser'),)
