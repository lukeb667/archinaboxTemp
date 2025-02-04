from django.contrib import admin
from .models import ArtifactModel
from .models import Filter

# Register your models here.
admin.site.register(ArtifactModel)
admin.site.register(Filter)