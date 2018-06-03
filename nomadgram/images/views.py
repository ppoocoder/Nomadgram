# from django.shortcuts import render   #템플릿을 사용하고 싶을떄 render 를 사용함
from rest_framework.views import APIView    # elemment를 다루고 가져오거나, 처리, method를 관리  위한 클래쓰 
from rest_framework.response import Response
from rest_framework import status
from . import models, serializers

# Create your views here.

class Feed(APIView):
    
    def get(self, request, format=None):
        

        user = request.user


        following_users = user.following.all()

        image_list =[]


        # print(following_users)

        for following_user in following_users:     
            
            user_images = following_user.images.all()[:2] #팔로잉 유저 리스트에 있는 유저의 이미지 중 가장 최근의 사진 2개를 불러오기 [:2]

            for image in user_images:    
                
                image_list.append(image)

        print(image_list)    


        sorted_list = sorted(image_list, key=lambda image: image.created_at,  reverse=True) 
          #sorted 전역함수 ([sorted할 list], key=[기준 attribute], reverse=True( (초기값: 업로드순) -> 최신순으로 순서 변경 활성화) )
          #get_key 함수 대처 ex) lambda x: x.attrs
        print(sorted_list)

        serializer = serializers.ImageSerializer(sorted_list, many=True)

        return Response(data=serializer.data)    


class LikeImage(APIView):
    def post(self,request,image_id, format=None):
        
        user = request.user
        
        try:
          found_image = models.Image.objects.get(id=image_id)
        except models.Image.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
       
        try:
            preexisiting_like = model.Like.object.get(
                creator=user,
                image=found_image
            )
        # refactoring -->>      
        #     preexisiting_like.delete()
        
            return Response(statu=status.HTTP_304_NOT_MODIFIED)
            #새로운 좋아요를 만들지 않겠다. ( unlike 를 따로 생성 필요)   
        except models.Like.DoesNotExist:

            new_like = models.Like.objects.create(
                    create=user,
                    image=found_image
            )
            new_like.save()

            return Response(status=200)  #create the url and the view 
class UnLikeImage(APIView):
    def delete(self, request, image_id, fomrmat=None):
        
        user = request.user
        try:
          found_image = models.Image.objects.get(id=image_id)
        except models.Image.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)         
         # -> image 찾기 

        try:
             preexisting_like = models.Like.objects.get(
                     create= user,
                     image=found_image
             )
             preexisting_like.delete()

             return Response(status=status.HTTP_204_NO_CONTENT)
        except models.Image.DoesNotExist:
             return Response(status=status.HTTP_304_NOT_NODIFIED)

class CommentOnImage(APIView):
    
    def post(self, request,image_id, format=None):
        
        # print(request.data)
        
        user = request.user
           #해당 이미지를 찾아서 이미지와 시리얼 라이저를 저장
        try:       
            found_image = models.Image.objects.get(id=image_id)
        except models.Image.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
            
        serializer = serializers.CommentSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save(creator=user, image=found_image)

            return Response(data=serializer.data, status=status.HTTP_201_CREATED ) #메세지 필드와 함께 댓글을 생성    
            # print('im valid')

        else:
            
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Comment(APIView):
    
    def delete(self, request, comment_id, format=None):
        user= request.user
        try:
            commet = models.Comment.objects.get(id=comment_id, creator=user)
            commet.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except models.Comment.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)    

# def get_key(image):
#     return image.created_at  
# -> lambda x을 이용해서 함수대신 사용함 
 

# class  ListAllImages(APIView):
    
#     def get(self, request, format=None): # self ==  self attributes , request == get, post, put delete  format= json  또는 xml 로 변경 가능 None 은 자동적으로 json으로 처리

#         all_images = models.Image.objects.all()

#         serializer = serializers.ImageSerializer(all_images, many=True)

#         return Response(data=serializer.data)



# class ListAllComments(APIView):

#     def get(self, request, format=None):
#         all_comments = models.Comment.objects.all() # all() objects 에 쌓인 comments 전체를 가져옴 filter()을 써서 query를 바꿀수 있음
        
#         serializer = serializers.CommentSerializer(all_comments, many=True)

#         return Response(data=serializer.data)



# class ListAllLikes(APIView):
    
#     def get(self, request, format=None):

#         all_likes = models.Like.objects.all()

#         serializer =serializers.LikeSerializer(all_likes, many=True)

#         return Response(data=serializer.data)