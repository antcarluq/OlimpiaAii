from BiKlopp.populate import popular_jugadores_mercado, populate_news
from BiKlopp.models import Equipo, Jugador, Mercado
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from BiKlopp.news import filter_by_player_and_team, filter_by_team, filter_by_player_or_team

def popularJugadoresMercado(request):
    popular_jugadores_mercado("dcamalv@gmail.com", "contraseña")
    return HttpResponseRedirect('/admin/')

def popular_noticias(request):
    populate_news()

def index(request):
    return render(request, "index.html")

def recomendar(request):
    correo = request.POST['correo']
    contrasenya = request.POST['contrasenya']
    #actualizar_info = request.POST['actualizar_info']
    #TODO popular_jugadores_mercado(correo, contrasenya, actualizar_info)
    #popular_jugadores_mercado(correo, contrasenya)
    #TODO popular_jugadores_mi_equipo(correo, contrasenya)
    #TODO algoritmo_recomendacion()
    jugadores = Jugador.objects.all() #Provisional: Se sustituyen por los jugadores recomendados
    #Todo solucionar lo de las URL
    return render(request, "recomendados.html", {"jugadores": jugadores})
