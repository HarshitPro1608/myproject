from django.urls import path
from .views import ClientList, ClientDetail, ArtistList, ArtistDetail, WorkList, WorkDetail,UserList

urlpatterns = [
    path('users/', UserList.as_view(), name='user-list'),
    path('clients/', ClientList.as_view()),
    path('clients/<int:pk>/', ClientDetail.as_view()),
    path('artists/', ArtistList.as_view()),
    path('artists/<int:pk>/', ArtistDetail.as_view()),
    path('works/', WorkList.as_view()),
    path('works/<int:pk>/', WorkDetail.as_view()),
]
