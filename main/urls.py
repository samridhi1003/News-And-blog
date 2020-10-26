from django.urls import path,include
from . import views
urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('accounts/',include('accounts.urls')),
    path('',views.myhome,name='newspage')
]