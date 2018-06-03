from rest_framework.views import APIView   
from rest_framework.response import Response
from rest_framework import status
from . import models, serializers



class ExploreUser(APIView):

    def get(self, request, format=None):
        last_five = models.User.objects.all().order_by('-data_joined')[:5]

        serializer = serializers.ExplorUserSerializer(last_five, many= True)

        return Response(data=serializer.data, status=status.HTTP_200_OK)

class FollowUser(APIView):
    def get(self, request, format=None):

        user = request.user #follow 할려는 유저(요청하는 유저) 
        try:
            user_to_follow = models.User.objects.get(id=user_id)
        except models.User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        user.following.add(user_to_follow) # 요청하는 유저의 id 를 MODEL에서 불러와서 following 리스트에 add (추가)  
        user.save()

        return Response(status=status.HTTP_200_OK)


class UnFollowUser(APIView):
    def get(self, request, format=None):

        user = request.user #follow 할려는 유저(요청하는 유저) 
        try:
            user_to_follow = models.User.objects.get(id=user_id)
        except models.User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        user.following.remove(user_to_follow) # 요청하는 유저의 id 를 MODEL에서 불러와서 following 리스트에 remove (제거)  
        user.save()

        return Response(status=status.HTTP_200_OK)


# from django.contrib.auth.mixins import LoginRequiredMixin
# from django.urls import reverse
# from django.views.generic import DetailView, ListView, RedirectView, UpdateView

# from .models import User


# class UserDetailView(LoginRequiredMixin, DetailView):
#     model = User
#     # These next two lines tell the view to index lookups by username
#     slug_field = 'username'
#     slug_url_kwarg = 'username'


# class UserRedirectView(LoginRequiredMixin, RedirectView):
#     permanent = False

#     def get_redirect_url(self):
#         return reverse('users:detail',
#                        kwargs={'username': self.request.user.username})


# class UserUpdateView(LoginRequiredMixin, UpdateView):

#     fields = ['name', ]

#     # we already imported User in the view code above, remember?
#     model = User

#     # send the user back to their own page after a successful update
#     def get_success_url(self):
#         return reverse('users:detail',
#                        kwargs={'username': self.request.user.username})

#     def get_object(self):
#         # Only get the User record for the user making the request
#         return User.objects.get(username=self.request.user.username)


# class UserListView(LoginRequiredMixin, ListView):
#     model = User
#     # These next two lines tell the view to index lookups by username
#     slug_field = 'username'
#     slug_url_kwarg = 'username'
