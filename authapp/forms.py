from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = get_user_model()
        fields = (
            'username',
            'phone',
            'email',
            'first_name',
            'last_name',
            'avatar'
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = "input-form"


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = get_user_model()
        fields = (
            'username',
            'phone',
            'email',
            'first_name',
            'last_name',
            'avatar'
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = "input-form"
