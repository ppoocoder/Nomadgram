from rest_framework import serializers
from . import models
from nomadgram.users import models as user_models


class FeedUserSerializer(serializers.ModelSerializer):
     
     class Meta:
         model = user_models.User
         fields = (
             'username',
             'profile_image',
         )


class CommentSerializer(serializers.ModelSerializer):
        
    creator = FeedUserSerializer(read_only=True)

    class Meta:
        model = models.Comment
        fields = (
            'id',     #(1) id는 변경이 불가능하고
            'message',    #(3) 찾을 필드는 메세지 밖에 없음
            'creator',   #(2)creator 는 'read_only' 로 읽기만 가능하기 때문에
        )


class LikeSerializer(serializers.ModelSerializer):

      

    class Meta:
        model = models.Like
        fields = '__all__'      # '__all__' 모든 필드의 값을 가져오다는 명령어 . Image.all 





class ImageSerializer(serializers.ModelSerializer):

    comments = CommentSerializer(many=True)
    # likes = LikeSerializer(many=True)
    creator = FeedUserSerializer()

    class Meta:
        model = models.Image
        fields = (
            'id',
            'file',
            'location',
            'caption',
            'comments',
            'like_count',    
            'creator',
        )   


                