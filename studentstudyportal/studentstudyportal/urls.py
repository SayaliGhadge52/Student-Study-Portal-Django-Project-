"""studentstudyportal URL Configuration

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
from django.urls.conf import include
from dashboard import views
from dashboard import views as dash_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home,name='home'),
    path('notes', views.notes,name="notes"),
    path('delete_note/<int:pk>', views.delete_note,name="delete-note"),
    path('notes_detail/<int:pk>', views.NotesDetailView.as_view(),name="notes-detail"),
    path('homework', views.homework,name="homework"),
    path('update_homework/<int:pk>', views.update_homework,name="update-homework"),
    path('delete_homework/<int:pk>', views.delete_homework,name="delete-homework"),
    path('youtube', views.youtube,name="youtube"),
    path('todo', views.todo,name="todo"),
    path('update_todo/<int:pk>', views.update_todo,name="update-todo"),
    path('delete_todo/<int:pk>', views.delete_todo,name="delete-todo"),
    path('login/',auth_views.LoginView.as_view(template_name="dashboard/login.html"), name='login'),
    path('profile',views.profile,name='profile'),
    path('register/',dash_views.register, name='register'),
    path('logout/',auth_views.LogoutView.as_view(template_name="dashboard/logout.html"), name='logout'),
]
