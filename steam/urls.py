from django.urls import path  # Importa o módulo para definir URLs
from .views import steam_library_view, export_games_to_excel # Importa as views da aplicação

urlpatterns = [
    # URL para visualizar a biblioteca Steam
    path('library/', steam_library_view, name='steam-library-page'),

    # URL para exportar os jogos para um arquivo Excel
    path('export-games/', export_games_to_excel, name='export_games'),
]

