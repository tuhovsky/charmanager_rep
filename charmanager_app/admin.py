from django.contrib import admin

from .models import UserCharacter, Skill


class UserCharacterAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Dates Information', {
         'fields': ['date_joined', 'last_login']}),
        ('User', {
         'fields': ['username', 'email', 'password']}),
        ('Character', {'fields': ['nickname', 'gender', 'specialization',
                                  'level', 'skills']}),
    ]
    list_display = ('username', 'email', 'nickname', 'last_login')
    list_filter = ['gender', 'specialization', 'level']
    search_fields = ['nickname', 'username', 'email']
    list_per_page = 10
    filter_horizontal = ('skills', )


class SkillAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')
    search_fields = ['title', 'description']
    list_per_page = 10


admin.site.register(UserCharacter, UserCharacterAdmin)
admin.site.register(Skill, SkillAdmin)

# Register your models here.
