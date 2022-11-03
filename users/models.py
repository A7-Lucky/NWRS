from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)

class UserManager(BaseUserManager):
    def create_user(self, username, password=None):
        if not username:
            raise ValueError('Users must have an username')

        user = self.model(
            username=username
            )

        # user = self.model(
        #     email=self.normalize_email(email),
        # )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password=None):
        user = self.create_user(
            username,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    username = models.CharField(verbose_name='username', max_length=50, unique=True,)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin
    

class Profile(models.Model):
    user = models.OneToOneField(User, verbose_name=(""), on_delete=models.CASCADE)
    profile_img = models.ImageField(blank = True, default="", upload_to="")
    introduce = models.CharField(max_length = 30)
    favorite = models.CharField(max_length = 30)
    
    def __str__(self):
        return str(self.user)
