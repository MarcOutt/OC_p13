from django.contrib import admin
from django.urls import path
from lettings import views
from lettings.views import letting
from oc_lettings_site.views import index, trigger_error
from profiles.views import profiles_index, profile


urlpatterns = [
    path('', index, name='index'),
    path('sentry-debug/', trigger_error),
    path('lettings/', views.index, name='lettings_index'),
    path('lettings/<int:letting_id>/', letting, name='letting'),
    path('profiles/', profiles_index, name='profiles_index'),
    path('profiles/<str:username>/', profile, name='profile'),
    path('admin/', admin.site.urls),
]
