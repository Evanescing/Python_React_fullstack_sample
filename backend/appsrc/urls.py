from django.urls import include, path

from .views.user_to_trainer import UserToTrainer, UserSendRequest, UserGetRequest


urlpatterns = [
    path('user/totrainer', UserToTrainer.as_view(), name='change_role'),
    path('user/totrainer/getrequest', UserGetRequest.as_view()),
    path('user/totrainer/sendrequest', UserSendRequest.as_view(), name='sendrequest')
]
