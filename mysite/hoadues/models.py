from django.db import models
from datetime import datetime

#Custom's User without Username
from django.contrib.auth.models import AbstractUser
#from django.utils.translation import ugettext_lazy as _

#Let Manager Know
from django.contrib.auth.models import BaseUserManager



#Class Managger
class UserManager(BaseUserManager):
    """Define a model manager for User model with no username field."""

    use_in_migrations = True

    def _create_user(self, email, password):
        """Create and save a User with the given email and password."""
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user



    def _create_user(self, email, password,  **extra_fields):
        """Create and save a User with the given email and password."""
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        """Create and save a regular User with the given email and password."""
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)




class User(AbstractUser):
    """User model."""

#Remove User Name Field
    username = None
#Make the email field required and unique
    email = models.EmailField(('email address'), unique=True)
#Going to Email to replace username Field
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

#Let the Mangager know
    objects = UserManager() ## This is the new line in the User model. ##


class Address(models.Model):
    lot = models.IntegerField()
    street_num = models.IntegerField()
    street = models.CharField(max_length=200)
    #owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return "Lot: "+str(self.lot)







# Create your models here.
# Create your models here.
class Bill(models.Model):
    dscpt_text=models.CharField(max_length=200)
    issue_date = models.DateField(auto_now_add= True, verbose_name=("Creation date"))
    due_date = models.DateField(verbose_name=("Due date"))
    amt = models.DecimalField(decimal_places=2, max_digits=20)
    paid = models.BooleanField(default=False)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.dscpt_text + " " + self.issue_date.strftime("%m/%d/%Y, %H:%M:%S") + " " + self.due_date.strftime("%m/%d/%Y, %H:%M:%S") + " " + str(self.amt)
