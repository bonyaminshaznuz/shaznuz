from django.contrib import admin
from .models import *

admin.site.register(EducationAndTraining)
admin.site.register(SkillCategory)
admin.site.register(MySkill)
admin.site.register(MyProject)

class WebsiteAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        if Website.objects.exists():
            return False 
        return True  

admin.site.register(Website, WebsiteAdmin)
admin.site.register(HeroInfo,WebsiteAdmin)
admin.site.register(Footer)
admin.site.register(SocialIcon)