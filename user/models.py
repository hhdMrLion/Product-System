from django.db import models

# Create your models here.


class User(models.Model):
    name = models.CharField('用户名', max_length=128, unique=True)
    password = models.CharField('密码', max_length=256)
    created_time = models.DateTimeField('创建时间', auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-created_time']
        verbose_name = verbose_name_plural = '用户'
        db_table = 'user'