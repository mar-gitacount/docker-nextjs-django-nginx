from django.contrib import admin
from .models import Todo ,WatchItem,Watch,BuchererItem

# Register your models here.


admin.site.register(Todo)
admin.site.register(WatchItem)
admin.site.register(Watch)
admin.site.register(BuchererItem)