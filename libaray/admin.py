from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserChangeForm , CustomUserCreationForm

from .models import CustomUser,book
class CustomUserAdmin(UserAdmin):
    add_form =CustomUserCreationForm
    form =CustomUserChangeForm
    model = CustomUser
    list_display=['username','is_staff','email','is_superuser','password']


admin.site.register(CustomUser,CustomUserAdmin)

class bookAdmin(admin.ModelAdmin):
    model="book"
    list_display=["bookname","author"]

admin.site.register(book,bookAdmin)
    