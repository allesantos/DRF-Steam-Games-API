from django.shortcuts import render
import requests
from .models import Game
from django.conf import settings
from django.http import HttpResponse
from openpyxl import Workbook

# Sua Steam API Key
STEAM_API_KEY = settings.STEAM_API_KEY

def steam_library_view(request):
    """
    View para renderizar a página de consulta de jogos na Steam.
    """
    error = None
    games = None
    search_query = request.GET.get('search', '')  # Termo de busca

    # Verificar se o Steam ID foi fornecido via GET
    steam_id = request.GET.get('steam_id')
    if steam_id:
        # URL da API Steam para buscar jogos
        url = f"http://api.steampowered.com/IPlayerService/GetOwnedGames/v1/"
        params = {
            "key": STEAM_API_KEY,
            "steamid": steam_id,
            "include_appinfo": True,  # Inclui informações detalhadas dos jogos
            "include_played_free_games": True
        }

        try:
            response = requests.get(url, params=params)
            data = response.json()

            # Verificar se a resposta contém jogos
            if "response" not in data or "games" not in data["response"]:
                error = "Nenhum jogo encontrado ou Steam ID inválido."
            else:
                # Obter jogos da API
                games = data["response"]["games"]

                # Salvar ou atualizar os jogos no banco de dados
                for game in games:
                    Game.objects.update_or_create(
                        steam_id=steam_id,
                        appid=game['appid'],
                        defaults={
                            'name': game.get('name', ''),
                            'tempo_jogado': game.get('playtime_forever', 0),
                            'img_icon_url': game.get('img_icon_url', '')
                        }
                    )

                # Recuperar jogos do banco de dados
                games = Game.objects.filter(steam_id=steam_id)
                if search_query:
                    games = games.filter(name__icontains=search_query)

                # Adicionar tempo jogado em horas a cada jogo
                for game in games:
                    horas = game.tempo_jogado // 60  # Parte inteira das horas
                    minutos = game.tempo_jogado % 60  # Minutos restantes
                    game.tempo_jogado_formatado = f"{horas} horas e {minutos} min" if horas > 0 else f"{minutos} min"

        except Exception as e:
            error = f"Ocorreu um erro: {str(e)}"

    # Renderizar o template com os jogos ou mensagem de erro
    return render(request, 'steam/steam_library.html', {'error': error, 'games': games})

def export_games_to_excel(request):
    # Obter o Steam ID da query string
    steam_id = request.GET.get('steam_id')
    if not steam_id:
        return HttpResponse("Steam ID is required", status=400)

    # Recuperar os jogos do banco de dados
    games = Game.objects.filter(steam_id=steam_id)

    if not games.exists():
        return HttpResponse("No games found for this Steam ID", status=404)

    # Criar um arquivo Excel
    workbook = Workbook()
    sheet = workbook.active
    sheet.title = "Steam Games"

    # Cabeçalhos
    sheet.append(["Nome do Jogo", "Tempo Jogado (minutos)"])

    # Adicionar dados dos jogos
    for game in games:
        sheet.append([game.name, game.tempo_jogado])

    # Configurar a resposta HTTP para baixar o arquivo
    response = HttpResponse(
        content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
    )
    response['Content-Disposition'] = 'attachment; filename="steam_games.xlsx"'
    workbook.save(response)

    return response
