from django.urls import path
from .views import remind

# 画像用
from django.conf import settings
from django.conf.urls.static import static

app_name = 'jusbe'

urlpatterns = [
    path('', remind.IndexView.as_view(), name="index"),
]

# 画像用
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
