from django.urls import path
from apps.bancoPregunta.views import *
# from apps.locations.apiViews import *
from apps.bancoPregunta.views import *

urlpatterns = [
    path('readResultados/', read_resultado_view, name='readResultados'),
    path('createPregunta/', create_pregunta_view, name='createPregunta')
    # path('readDepartament/', read_departament_view, name='readDepartament'),
    # path('readCity/', read_city_view, name='readCity'),
    # path('readOffice/', read_office_view, name='readOffice'),
    # path('createOffice/',create_office_view, name='createOffice'),
	# path('updateOffice/<int:pk>',update_office_view, name='updateOffice'),
    #------------URLS APIS----------------------------------------------
	# path('apiDepartament',api_departament, name='apiDepartament'),
	# path('apiCity',api_city, name='apiCity'),
    # path('apiOffice',api_office, name='apiOffice'),
    # path('apiOffice/<int:pk>',api_office, name='apiOffice'),

    
]