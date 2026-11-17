from django import forms
from .models import Donor, Recipient, Hospital, Donation, BloodUnit, BloodTest, BloodRequest, CollectionSite


class DonorForm(forms.ModelForm):

    class Meta:
        model = Donor

        fields = [
            'firstname',
            'lastname',
            'age',
            'bloodtype',
            'address',
            'phone',
            'email',
            'status',
        ]

        widgets = {
            'firstname': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter first name'
            }),

            'lastname': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter last name'
            }),

            'age': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter age'
            }),

            'bloodtype': forms.Select(attrs={
                'class': 'form-control'
            }),

            'address': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter address'
            }),

            'phone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter phone number'
            }),

            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter email address'
            }),

            'status': forms.Select(attrs={
                'class': 'form-control'
            }),
        }



class RecipientForm(forms.ModelForm):

    class Meta:
        model = Recipient

        fields = [
            'firstname',
            'lastname',
            'age',
            'bloodtype',
            'address',
            'phone'
        ]

        widgets = {
            'firstname': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter first name'
            }),

            'lastname': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter last name'
            }),

            'age': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter age'
            }),

            'bloodtype': forms.Select(attrs={
                'class': 'form-control'
            }),

            'address': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter address'
            }),

            'phone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter phone number'
            }),
        }



class HospitalForm(forms.ModelForm):

    class Meta:
        model = Hospital

        fields = [
            'name',
            'address',
            'contact',
            'email'
        ]

        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter hospital name'
            }),

            'address': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter hospital address'
            }),

            'contact': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter contact number'
            }),

            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter hospital email'
            }),
        }


      
class DonationForm(forms.ModelForm):

    class Meta:
        model = Donation

        fields = [
            'donor',
            'bloodtype',
            'collectionsite',
            'donationdate'
        ]

        widgets = {
            'donor': forms.Select(attrs={
                'class': 'form-control'
            }),

            'bloodtype': forms.Select(attrs={
                'class': 'form-control'
            }),

            'collectionsite': forms.Select(attrs={
                'class': 'form-control'
            }),

            'donationdate': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
        }  


class BloodUnitForm(forms.ModelForm):

    class Meta:
        model = BloodUnit

        fields = [
            'donation',
            'volume',
            'expirydate',
            'status'
        ]

        widgets = {
            'donation': forms.Select(attrs={
                'class': 'form-control'
            }),

            'volume': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter volume in ml'
            }),

            'expirydate': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),

            'status': forms.Select(attrs={
                'class': 'form-control'
            }),
        }




class BloodTestForm(forms.ModelForm):

    class Meta:
        model = BloodTest

        fields = [
            'bloodunit',
            'testtype',
            'testresult',
            'labtechnician',
            'remarks'
        ]

        widgets = {
            'bloodunit': forms.Select(attrs={
                'class': 'form-control'
            }),

            'testtype': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter test type'
            }),

            'testresult': forms.Select(attrs={
                'class': 'form-control'
            }),

            'labtechnician': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter laboratory technician name'
            }),

            'remarks': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Enter additional remarks'
            }),
        }
        

class BloodRequestForm(forms.ModelForm):

    class Meta:
        model = BloodRequest
        fields = [
            'hospital',
            'recipient',
            'bloodtype',
            'unitsrequired',
            'priority',
            'status'
        ]

        widgets = {
            'hospital': forms.Select(attrs={
                'class': 'form-control'
            }),

            'recipient': forms.Select(attrs={
                'class': 'form-control'
            }),

            'bloodtype': forms.Select(attrs={
                'class': 'form-control'
            }),

            'unitsrequired': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': 1,
                'placeholder': 'Enter number of units required'
            }),

            'priority': forms.Select(attrs={
                'class': 'form-control'
            }),

            'status': forms.Select(attrs={
                'class': 'form-control'
            }),
        }

class CollectionSiteForm(forms.ModelForm):

    class Meta:
        model = CollectionSite

        fields = [
            'name',
            'location'
        ]

        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter collection site name'
            }),

            'location': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter collection site location'
            }),
        }