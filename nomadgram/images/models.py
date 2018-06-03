from django.db import models
from nomadgram.users import models as user_models
# Create your models here.

class TimeStampedModel(models.Model):

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Image(TimeStampedModel):     

    """ Image Model"""

    file = models.ImageField()
    location =models.CharField(max_length=140)
    caption = models.TextField()
    creator = models.ForeignKey(user_models.User, on_delete=models.CASCADE, null=True, related_name='images')

    @property       # 모델 필드인데, 데이터로 가지는 않지만 모델안에 존재함
    def like_count(self):
        return self.likes.all().count()


    def __str__(self):   #문자열화 함수 크래스를 실행시 def __str__(self): 함수가 실행됨 
        return '{} -{}'.format(self.location, self.caption)

    class Meta:
        ordering = ['-created_at']       # 내가 db에서 얻은 리스트를 생성된 날짜로 정렬할때  Meta class로 설정




class Comment(TimeStampedModel):

    """ Comment Model"""

    message = models.TextField()
    creator =models.ForeignKey(user_models.User, on_delete=models.CASCADE, null=True)
    image = models.ForeignKey(Image, on_delete=models.CASCADE, null=True, related_name='comments')

    def __str__(self):
        return self.message

class Like(TimeStampedModel):
    
    """ Like Model """

    creator = models.ForeignKey(user_models.User, on_delete=models.CASCADE, null=True)
    image = models.ForeignKey(Image, on_delete=models.CASCADE, null=True, related_name='likes')


    def __str__(self):
        return 'User: {}- Image Caption: {}'.format(self.creator.username, self.image.caption)   #{}-{}.format(arg1, arg2) :: python 문법