from django import forms
from .models import Vendor, MarketApplicant, Blog
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["first_name", "email", "username", "password1", "password2"]
        labels = {
            "first_name": "Name",
        }


class VendorForm(forms.ModelForm):
    class Meta:
        model = Vendor
        fields = [
            "name",
            "phone_number",
            "social_media_alias",
            "description",
            "ssm_no",
            "product_name",
            "product_type",
            "product_picture",
            "menu",
        ]


class MarketApplicantForm(forms.ModelForm):
    class Meta:
        model = MarketApplicant
        fields = ["slot", "certificate", "equipment_list"]


class UploadPaymentForm(forms.ModelForm):
    class Meta:
        model = MarketApplicant
        fields = ["proof_of_payment"]


class VendorPageForm(forms.ModelForm):
    class Meta:
        model = Vendor
        fields = [
            "name",
            "phone_number",
            "social_media_alias",
            "description",
            "ssm_no",
            "product_name",
            "product_type",
            "product_picture",
            "menu",
        ]
        labels = {
            "ssm_no": "SSM Number",
        }


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ["title", "content"]
