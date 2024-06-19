from django.urls import path
from .views import home_view, follow, like, profile_view, settings_view, create_post

urlpatterns = [
    path('', home_view),
    path('follow/', follow),
    path('like/', like),
    path('profile/<int:a>', profile_view),
    path('settings/', settings_view),
    path('create_post/', create_post),
]


