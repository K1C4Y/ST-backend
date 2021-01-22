from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Test)
admin.site.register(OpenQuestion)
admin.site.register(ClosedQuestion)
admin.site.register(Answer)
admin.site.register(TestAnswer)
admin.site.register(CQAnswer)
admin.site.register(OQAnswer)
