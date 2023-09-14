from django.contrib import admin
from .models import Users, Coords, Images, PerevalAdded, ActivityTypes, Areas

admin.site.register(Users)
admin.site.register(Coords)
admin.site.register(Images)
admin.site.register(PerevalAdded)
admin.site.register(ActivityTypes)
admin.site.register(Areas)
