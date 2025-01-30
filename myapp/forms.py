from django import forms
from django.contrib.auth.models import User
from .models import Student

class StudentRegistrationForm(forms.ModelForm):
    admission_number = forms.CharField(max_length=20, help_text="Enter your admission number")
    name = forms.CharField(max_length=100, help_text="Enter your full name")
    password = forms.CharField(widget=forms.PasswordInput, help_text="Enter a strong password")

    class Meta:
        model = User
        fields = ['admission_number', 'name', 'password']

    def clean(self):
        cleaned_data = super().clean()
        admission_number = cleaned_data.get("admission_number")
        name = cleaned_data.get("name")

        # Check if admission number exists
        try:
            student = Student.objects.get(admission_number=admission_number)
        except Student.DoesNotExist:
            raise forms.ValidationError("Admission number does not exist.")

        # Ensure the name matches the student’s actual name
        if student.name.lower() != name.lower():
            raise forms.ValidationError("Name does not match our records.")

        return cleaned_data



# forms.py
from django import forms
from .models import Student

class StudentProfileEditForm(forms.ModelForm):
    class Meta:
        model = Student
        # Only include fields that are safe for students to edit
        fields = [
            'address',
            'emergency_contact_name',
            'emergency_contact_phone',
            'emergency_contact_relationship',
            'medical_conditions',
            'blood_group'
        ]
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Add Bootstrap classes and placeholders
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control',
                'placeholder': self.fields[field].label
            })