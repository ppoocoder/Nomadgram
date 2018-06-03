from django.contrib import admin
from . import models # . 현재 폴더 전체를 의미
# Register your models here.

@admin.register(models.Image)
class ImageAdmin(admin.ModelAdmin):
   
    list_display_links =(
    'location',
    
    )

    search_fields =(
    'location',
    'caption',
    ) #검색기능 추가 

    list_filter =(

        'location',
        'creator', 
    ) #필터 추가 

    list_display = (    #파이썬 admin 옵션 해당 파라미터의 리스트를 찍어줌 
         'file',
         'location',
         'caption',
         'creator',   
         'created_at',
         'updated_at',
    )
@admin.register(models.Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ( #Django admin 옵션 해당 파라미터의 리스트를 찍어줌 {list_display, list_filter, search_fields, list_display_links}
       
         'creator',   
         'image',
         'created_at',
         'updated_at',
    )



@admin.register(models.Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = (   #파이썬 admin 옵션 해당 파라미터의 리스트를 찍어줌 
         'message',
         'creator',   
         'image',
         'created_at',
         'updated_at',
    )
        