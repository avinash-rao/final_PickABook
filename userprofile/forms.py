from django.contrib.auth.models import User
from django import forms
from django.forms import ModelForm


class UpdateProfile(forms.ModelForm):
    # username = forms.CharField(required=True)

    # id = forms.HiddenInput()
    email = forms.EmailField(required=True, widget=forms.TextInput(attrs={'readonly':'readonly'}))
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)

    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name')

    def clean_email(self):
        # username = self.cleaned_data.get('username')
        email = self.cleaned_data.get('email')

        # if email and User.objects.filter(email=email).exclude(username=username).count():
        #     raise forms.ValidationError('This email address is already in use. Please supply a different email address.')
        return email

    # def save(self, commit=True):
    #     user = super(RegistrationForm, self).save(commit=False)
    #     user.email = self.cleaned_data['email']
    #
    #     if commit:
    #         user.save()
    #
    #     return user
