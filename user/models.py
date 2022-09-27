from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager


class UserManager(BaseUserManager):    
   
   use_in_migrations = True    
   
   def create_user(self, email, organization, password):        
       
       if not email:            
           raise ValueError('must have user email')
       if not password:            
           raise ValueError('must have user password')

       user = self.model(            
           email=self.normalize_email(email),
           organization=organization              
       )        
       user.set_password(password)        
       user.save(using=self._db)        
       return user

   def create_superuser(self, email, organization, password):        
   
       user = self.create_user(            
           email = self.normalize_email(email),
           organization=organization,                       
           password=password        
       )
       user.is_admin = True
       user.is_superuser = True
       user.save(using=self._db)
       return user 


class User(AbstractBaseUser, PermissionsMixin):    
    """
        유저 프로파일 사진
        유저 닉네임     -> 화면에 표기되는 이름
        유저 이름       -> 실제 사용자 이름
        유저 이메일주소 -> 회원가입할때 사용하는 아이디
        유저 비밀번호 -> 디폴트 쓰자
    """
   
    objects = UserManager()
   
    email = models.EmailField(        
       max_length=255,        
       unique=True,    
    )
    # organization = models.CharField(max_length=30)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    profile_image = models.TextField()  # 프로필 이미지
    nickname = models.CharField(max_length=24)
    username = models.CharField(max_length=24)
    USERNAME_FIELD = 'email'    

    def __str__(self):
        return self.email

    @property
    def is_staff(self):
        return self.is_admin
    class Meta:
        db_table = "User"