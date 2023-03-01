from django.forms import ModelForm

from masterapp.models import Master


class UpdateMasterDetailForm(ModelForm):
    class Meta:
        model = Master
        fields = ('about_me', 'master_profissions')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = "input-form"