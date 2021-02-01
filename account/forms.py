from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate

from account.models import Account


class RegistrationForm(UserCreationForm):
    employeId = forms.CharField(max_length=30, help_text='Required', widget=forms.TextInput(attrs={
        "class" : "shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline",
        "type" : "text",
        "placeholder" : "Employe ID"
    }))
    full_name = forms.CharField(max_length=30, help_text='Required', widget=forms.TextInput(attrs={
        "class" : "shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline",
        "type" : "text",
        "placeholder" : "Full Name"
    }))
    Department = forms.CharField(max_length=30, help_text='Required', widget=forms.TextInput(attrs={
        "class" : "shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline",
        "type" : "text",
        "placeholder" : "Department Name"
    }))
    password1 = forms.CharField(max_length=30, help_text='Required', widget=forms.TextInput(attrs={
        "class" : "shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline",
        "type" : "password",
        "placeholder" : "Password"
    }))
    password2 = forms.CharField(max_length=30, help_text='Required', widget=forms.TextInput(attrs={
        "class" : "shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline",
        "type" : "password",
        "placeholder" : "Confirm Password"
    }))
    class Meta:
        model = Account
        fields = ('employeId', 'full_name','Department', 'password1', 'password2', )


class AccountAuthenticationForm(forms.ModelForm):

    employeId = forms.CharField(max_length=30, help_text='Required', widget=forms.TextInput(attrs={
        "class" : "shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline",
        "type" : "text",
        "placeholder" : "Employe ID"
    }))
    password = forms.CharField(max_length=30, help_text='Required', widget=forms.TextInput(attrs={
        "class" : "shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline",
        "type" : "password",
        "placeholder" : "Password"
    }))

    class Meta:
        model = Account
        fields = ('employeId', 'password')

    def clean(self):
        if self.is_valid():
            employeId = self.cleaned_data['employeId']
            password = self.cleaned_data['password']
            if not authenticate(employeId=employeId, password=password):
                raise forms.ValidationError("Invalid login")

class UpdatePassword(UserCreationForm):
    employeId = forms.CharField(max_length=30, help_text='Required', widget=forms.TextInput(attrs={
        "class" : "shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline",
        "type" : "text",
        "placeholder" : "Employe ID"
    }))
    password = forms.CharField(max_length=30, help_text='Required', widget=forms.TextInput(attrs={
        "class" : "shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline",
        "type" : "password",
        "placeholder" : "New Password"
    }))
    password2 = forms.CharField(max_length=30, help_text='Required', widget=forms.TextInput(attrs={
        "class" : "shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline",
        "type" : "password",
        "placeholder" : "Confirm Password"
    }))
    class Meta:
        model = Account
        fields = ('employeId','password', 'password2', )


class AccountUpdateForm(forms.ModelForm):

    class Meta:
        model = Account
        fields = ('employeId', 'full_name', 'Department')

    def clean_employeId(self):
        employeId = self.cleaned_data['employeId']
        try:
            account = Account.objects.exclude(pk=self.instance.pk).get(employeId=employeId)
        except Account.DoesNotExist:
            return employeId
        raise forms.ValidationError('employeId "%s" is already in use.' % account)

    def clean_full_name(self):
        full_name = self.cleaned_data['full_name']
        try:
            account = Account.objects.exclude(pk=self.instance.pk).get(full_name=full_name)
        except Account.DoesNotExist:
            return full_name
        raise forms.ValidationError('name "%s" is already in use.' % full_name)

    def clean_Department(self):
        Department = self.cleaned_data['Department']
        try:
            account = Account.objects.exclude(pk=self.instance.pk).get(Department=Department)
        except Account.DoesNotExist:
            return Department
        raise forms.ValidationError('name "%s" is already in use.' % Department)

    
