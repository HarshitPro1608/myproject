from django.urls import path
from .views import ClientList, ClientDetail, ArtistList, ArtistDetail, WorkList, WorkDetail,UserList
from . import views
urlpatterns = [
    path('/users', UserList.as_view(), name='users'),
    path('/clients', ClientList.as_view(),name='clients'),
    path('/clients/<int:pk>', ClientDetail.as_view()),
    path('/artists', ArtistList.as_view()),
    path('/artists/<int:pk>', ArtistDetail.as_view()),
    path('/works', WorkList.as_view()),
    path('/works/<int:pk>', WorkDetail.as_view()),
    path('/workss',views.work,name='blog-work'),
]
