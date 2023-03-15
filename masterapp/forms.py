from django.forms import ModelForm, Form, ChoiceField, CheckboxSelectMultiple, ModelMultipleChoiceField, \
    ModelChoiceField

from authapp.models import User
from masterapp.models import Master, CompletedWork


class UpdateUserForm(ModelForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'avatar', 'phone', 'email')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = "input-form"


class UpdateMasterDetailForm(ModelForm):
    class Meta:
        model = Master
        fields = ('about_me', 'master_profissions')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = "input-form"


class CompletedWorkCreateForm(ModelForm):
    class Meta:
        model = CompletedWork
        fields = ('photo', 'short_description', 'full_description', 'service_id', 'is_active')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = "input-form"


class CompletedWorkUpdateForm(ModelForm):
    class Meta:
        model = CompletedWork
        fields = ('photo', 'short_description', 'full_description', 'service_id', 'is_active')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = "input-form"
