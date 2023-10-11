from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from accounts.views import Aboutpageview
from accounts import views
from HeartHealth import settings

from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.user_login, name='user_login'),
    path('about/', Aboutpageview.as_view(), name='about'),
    path('accounts/', include('accounts.urls')),
    path('predict/', include('predict_risk.urls')),
]


urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
