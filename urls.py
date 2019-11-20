from django.contrib import admin
from django.urls import path
from database.views import chirpView

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', chirpView),
    path('index/', chirpView),
]

