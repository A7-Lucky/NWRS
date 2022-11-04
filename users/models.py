from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, username, password=None):
        if not username:
            raise ValueError('Users must have an username')

        user = self.model(
            username=self.username
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
    profile_img = models.ImageField(blank = True, default="", upload_to="")
    introduce = models.CharField(max_length = 200, blank = True)
    favorite = models.CharField(max_length = 100, blank = True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

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

# class User(AbstractBaseUser):
    # username = models.CharField(max_length = 20, unique=True)
    
    
    '''
    profile_img = models.ImageField(blank = True, default="", upload_to="")
    introduce = models.CharField(max_length = 200, blank = True)
    favorite = models.CharField(max_length = 100, blank = True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    '''
    
    # USERNAME_FIELD = 'username'