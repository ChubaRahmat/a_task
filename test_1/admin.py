from django.contrib import admin

# Register your models here.
from test_1.models import *

admin.site.register(Post)
admin.site.register(Comment)
