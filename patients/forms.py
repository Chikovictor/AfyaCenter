from django import forms
from patients.models import Appointment, Department, Doctor,Contact



class AppointmentForm(forms.ModelForm):  # links the form to the appointment model
    class Meta:
        model = Appointment
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
             'age': forms.NumberInput (attrs={'class': 'form-control'}),
             'address': forms.TextInput(attrs={'class': 'form-control'}),
             'appointment_date': forms.DateTimeInput(attrs={'class': 'form-control','type':'datetime-local'}),
            'department': forms.Select(attrs={'class': 'form-control'}),
            'doctor': forms.Select(attrs={'class': 'form-control'}),
            'application-time': forms.DateTimeInput(attrs={'class': 'form-control','type':'datetime-local'}),
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

# Filter active  departments,doctors en services for the dropdowns
        self.fields['department'].queryset = Department.objects.filter(is_active=True)
        self.fields['doctor'].queryset = Doctor.objects.filter(is_active=True)


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'
        widgets = {
            'name':forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'subject': forms.TextInput(attrs={'class': 'form-control'}),
            'message': forms.Textarea(attrs={'class': 'form-control'}),
        }
