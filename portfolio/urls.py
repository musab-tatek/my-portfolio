from django.contrib import admin
from django.urls import path, include
from django.http import Http404

urlpatterns = [
    path('admin/', admin.site.urls),
    path('' , include('main.urls'))
]
handler404 = 'main.views.view_404'
