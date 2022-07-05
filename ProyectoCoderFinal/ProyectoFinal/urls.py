from django.urls import path, include
from .views import *
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('',homeView, name = 'Home'),
    path('animeData/', animeData, name = 'Anime Data'),
    path('animeDelete/<int:id_anime>/', deleteAnime, name = 'Delete Anime'),
    path('editAnime/<int:id_anime>', editAnime, name = 'Edit Anime'),
    path('mangaData/', mangaData, name = 'Manga Data'),
    path('mangaDelete/<int:id_manga>/', deleteManga, name = 'Delete Manga'),
    path('editManga/<int:id_manga>', editManga, name = 'Edit Manga'),
    path('studioData/', studioData, name = 'Studio Data'),
    path('studioDelete/<int:id_studio>/', deleteStudio, name = 'Delete Studio'),
    path('editStudio/<int:id_studio>', editStudio, name = 'Edit Studio'),
    path('registerUser/', registerUser, name = 'Register'),
    path('loginUser/', loginRequest, name = 'Login'),
    path('logout/', LogoutView.as_view(), name = 'Logout'),
    path('profileDetails/',profile, name = 'Profile')

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
