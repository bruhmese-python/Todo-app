"""todo_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from todo_app import views

app_name = "todo_app"

handler500 = 'todo_app.views.handler404'
handler404 = 'todo_app.views.handler404'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', view=views.start, name='start'),
    path('save', view=views.save, name='save'),
    path('delete/<int:id>', view=views.delete, name='delete'),
    path('details_update/<int:id>',
         view=views.details_update, name='details_update'),
    path('update/<int:id>', view=views.update, name='update'),
    path('404', view=views.handler404, name='not_found'),
    path('viewdetails/<int:id>', view=views.viewdetails, name='viewdetails')

    # path('deleteedetails/<int:pk>',
    #      views.TaskDeleteView.as_view(), name='deletedetails'),

    # path('updatedetails/<int:pk>',
    #      views.TasUpdateView.as_view(), name='updatedetails'),


    # path('viewtask/', view=views.TaskListView.as_view(), name='viewtask')  but without any custom operations like ordering, name='viewtask')
    # path('viewtask/', view=views.start)
    # path('viewdetails/<int:pk>',
    #      view=views.TaskDetailView.as_view(), name='viewdetails')
]
