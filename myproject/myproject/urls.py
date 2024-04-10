from django.contrib import admin
from django.urls import path, include # <-- 1. add this 

urlpatterns = [
 
    path('admin/', admin.site.urls),

    # 2. add this line too
    path('', include('myapp.urls')),

]