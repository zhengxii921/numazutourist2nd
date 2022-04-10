from django.db import models
from django.contrib.auth.models import UserManager, AbstractUser

# Create your models here.

class CustomUserManager(UserManager):
    use_in_migrations = True

    def _create_user(self, email, username, password, **extra_fields):
        # create_user と create_superuser の共通処理
        if not email:
            raise ValueError('メールアドレスは必須です。')
        if not username:
            raise ValueError('ユーザー名は必須です。')

        user = self.model(email=email, username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user


    def create_user(self, username, email=None, password=None, **extra_fields):

        if not email:
            raise ValueError('メールアドレスは必須です。')
        if not username:
            raise ValueError('ユーザー名は必須です。')

        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)

        return self._create_user(email, username, password, **extra_fields)

    def create_superuser(self, username, email=None, password=None, **extra_fields):

        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, username, password, **extra_fields)

def icon_image_directory_path(instance, filename):
    return 'numazutourist/icon_images/{}.{}'.format(str(uuid.uuid4()), filename.split('.')[-1])

class CustomUser(AbstractUser):
    profile_picture = CloudinaryField("画像", folder=icon_image_directory_path, default="numazutourist/icon_default.png")
    objects = CustomUserManager()

    def __str__(self):
        return self.username