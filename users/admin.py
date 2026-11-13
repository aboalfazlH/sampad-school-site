from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import (
    User,
    Student,
    Teacher,
    Parents,
    Deputy,
    Manager,
    Consultant
)
from .forms import UserAdminCreationForm,UserAdminChangeForm

@admin.register(User)
class CUserAdmin(UserAdmin):
    form = UserAdminChangeForm
    add_form = UserAdminCreationForm

admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Parents)
admin.site.register(Deputy)
admin.site.register(Manager)
admin.site.register(Consultant)