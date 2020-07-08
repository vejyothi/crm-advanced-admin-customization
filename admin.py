from django.contrib import admin

# Register your models here.
from django.contrib import admin

# Register your models here.
from .models import roles,User,user_status, Contact_Status,Contact,task_status,todo_type,todo_desc,Notes
from django.contrib.admin.options import ModelAdmin
#from django.contrib.auth.admin import UserInline
from django.contrib.admin import TabularInline
# Register your models here.
class UserInline(admin.TabularInline):
    model=User

class UserAdmin(admin.ModelAdmin):
    list_display = ["name_title","name_first","name_middle","name_last","email"]
    search_fields = ["name_first","email"]
    list_filter = ["email"]
admin.site.register(User, UserAdmin)

class rolesAdmin(admin.ModelAdmin):
    model=roles
    inlines=[UserInline]
    list_display = ["roles_status"]
    search_fields = ["roles_status"]
    list_filter = ["roles_status"]
admin.site.register(roles, rolesAdmin)

class user_statusAdmin(admin.ModelAdmin):
    model=user_status
    inlines=[UserInline]
    list_display = ["status"]
    search_fields = ["status"]
    list_filter = ["status"]
admin.site.register(user_status, user_statusAdmin)
class NotesInline(admin.TabularInline):
    model=Notes

class NotesAdmin(admin.ModelAdmin):
    list_display = ["date","notes"]
    search_fields = ["notes"]
    list_filter = ["date"]
    
admin.site.register(Notes, NotesAdmin)

class ContactInline(admin.TabularInline):
    model=Contact
    
class ContactAdmin(admin.ModelAdmin):
    inlines=[NotesInline]
    list_display = ["contact_Title","company","industry"]
    search_fields = ["email"]
    list_filter = ["phone"]
admin.site.register(Contact, ContactAdmin)

class Contact_StatusAdmin(admin.ModelAdmin):
    models=Contact_Status
    inlines=[ContactInline]
    list_display = ["status"]
    search_fields = ["status"]
    list_filter = ["status"]
admin.site.register(Contact_Status, Contact_StatusAdmin)



class task_statusAdmin(admin.ModelAdmin):
    model=task_status
    inlines=[NotesInline]
    list_display = ["status"]
    search_fields = ["status"]
    list_filter = ["status"]
    
admin.site.register(task_status, task_statusAdmin)
class todo_typeAdmin(admin.ModelAdmin):
    model=todo_type
    inlines=[NotesInline]
    list_display = ["type"]
    search_fields = ["type"]
    list_filter = ["type"]
    
admin.site.register(todo_type, todo_typeAdmin)

class todo_descAdmin(admin.ModelAdmin):
    model=todo_desc
    inlines=[NotesInline]
    list_display = ["description"]
    search_fields = ["description"]
    list_filter = ["description"]
    
admin.site.register(todo_desc, todo_descAdmin)