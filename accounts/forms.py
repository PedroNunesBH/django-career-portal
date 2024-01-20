from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class UpgradeUserCreationForm(UserCreationForm):
    name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    profession = forms.CharField(max_length=50)
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ('name', 'last_name', 'profession', 'email', 'username', 'password1', 'password2')

    def save(self, commit=True):
        user = super(UpgradeUserCreationForm, self).save(commit=False)
        user.first_name = self.cleaned_data['name']
        user.last_name = self.cleaned_data['last_name']
        user.profession = self.cleaned_data['profession']
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
