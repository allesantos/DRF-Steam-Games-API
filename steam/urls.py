from django.urls import path
from .views import steam_library_view, export_games_to_excel

urlpatterns = [
    path('library/', steam_library_view, name='steam-library-page'),
    path('export-games/', export_games_to_excel, name='export_games'),

]

