from django import forms
from .models import AdmissionApplication, Department, Subject

class AdmissionForm(forms.ModelForm):
    class Meta:
        model = AdmissionApplication
        fields = ['full_name', 'email', 'phone', 'department', 'subject', 'preferred_date', 'photo']

        widgets = {
            'preferred_date': forms.DateInput(attrs={'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Make Subject initially empty until department is selected
        self.fields['subject'].queryset = Subject.objects.none()

        if 'department' in self.data:
            try:
                department_id = int(self.data.get('department'))
                self.fields['subject'].queryset = Subject.objects.filter(department_id=department_id)
            except (ValueError, TypeError):
                pass
        elif self.instance.pk:
            self.fields['subject'].queryset = self.instance.department.subjects.all()
