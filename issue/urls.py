from django.urls import path
from . import views
urlpatterns = [
    path('', views.hello_world),

    # here repoter end points
    path('create-reporter/', views.create_reporter), #--> This is for new reporte
    path("reporters/", views.reporters),
    
    # here issue end points
    path('issues/', views.issues), #--> This is for create issues
    path('all-issues/', views.all_issue) #--> This is for All issue
    #path('new-issue/', views.create_issue) #--> This is for new create issue

    


]   