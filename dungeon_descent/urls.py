from django.contrib import admin
from django.urls import path, include
from users.views import StatesView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('dj-rest-auth/', include('dj_rest_auth.urls')),
    path('dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')),
    path('states', StatesView.as_view()),
]
