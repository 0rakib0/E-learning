
from django.contrib.auth.models import BaseUserManager

class MyUserManager(BaseUserManager):    
    
    #create user by email and password
    def _create_user(self, email, password, **extra_fields):
        
        if not email:
            raise ValueError("Email must be set")
        
        email = self.normalize_email(email)
        user = self.model(email = email, **extra_fields)
        user.set_password(password)
        user.save(using =self._db)
        return user
    
    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('user_type','admin')
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        
        
        if extra_fields.get('is_staff') is not True:
            raise ValueError("Superuser Must have is_staff=True")
        
        if extra_fields.get('is_superuser') is not True:
            raise ValueError ('Superuser Must have is_superuser=True')

        return self._create_user(email, password, **extra_fields)
    