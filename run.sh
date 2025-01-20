#!/bin/bash
###
 # @File name: 
 # @Author: Tecot (tyx_cqbs@163.com)
 # @Version: V1.0
 # @Date: 2024-12-24 10:14:45
 # @Description: 
### 

source activate dsm

celery -A server worker --loglevel=info & 
python manage.py runserver 8173