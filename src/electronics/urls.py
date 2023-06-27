from django.contrib import admin
from django.urls import (
    include,
    path,
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/chain/', include('chain_store.urls')),
    path('api/employees/', include('employees.urls')),
]
