# from django.urls import path
# from .views import supporter_customuser, supporter_event, supporter_function, supporter_ticket, customer_event, customer_reservation, customer_function

# 画像用
from django.conf import settings
from django.conf.urls.static import static


app_name = 'jusbe'

urlpatterns = []

# 画像用
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
