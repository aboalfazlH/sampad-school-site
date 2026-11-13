from django.contrib.auth.forms import UserChangeForm,UserCreationForm
from .models import User


class UserAdminChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = "__all__"

class UserAdminCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = (
            "national_code",
            "phone_number",
            "email",
            "username",
            "first_name",
            "last_name",
            )