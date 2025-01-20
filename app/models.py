'''
File name: 
Author: Tecot (tyx_cqbs@163.com)
Version: V1.0
Date: 2024-12-12 10:52:15
Description: 
'''
from django.db import models
 
class TaskInfoModel(models.Model):
    STATUSES = ((0, 'success'), (1, 'faild'), (2, 'processing'))
    key = models.CharField(primary_key=True, verbose_name='key', max_length=64, default='')
    status = models.IntegerField(verbose_name='status', choices=STATUSES, default=2)
    
    class Meta:
        db_table = 'task_info'
        verbose_name = 'task_info'
        verbose_name_plural = 'task_info'
    