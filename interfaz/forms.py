from django import forms
from .models import Rbdms, HardwareType, OSType, Test

class TestForm(forms.ModelForm):
	class Meta:
		model = Test
		fields = '__all__'

		labels = {
			'rdbms': 'Seleccione el/los RDBMS',
			'hw_type': 'Configuración de hardware',
			'db_config': 'Configuración de base de datos',
			'os_type': 'Sistema Operativo',
		}

		widgets = {
			'rdbms': forms.CheckboxSelectMultiple(attrs={"class":"form-control"}),
			'hw_type': forms.Select(attrs={"class":"form-control"}), #queryset=HardwareType.objects.all().order_by('name')
			'hw_spec': forms.Textarea(attrs={'readonly':True, 'rows':8}),
			'db_config': forms.Select(attrs={"class":"form-control"}),
			'dbconf_spec': forms.Textarea(attrs={'readonly':True, 'rows':8}),
			'os_type': forms.Select(attrs={"class":"form-control"}),
		}


'''class TestForm(forms.Form):
	rdbms = forms.ModelMultipleChoiceField(queryset=Rbdms.objects.all(), widget=c
	hw_type = forms.ModelChoiceField(queryset=HardwareType.objects.all(), widget=forms.Select(attrs={"class":"form-control", 'required':True}))
	hw_spec = forms.CharField(widget=forms.Textarea(attrs={'readonly':True, 'rows':8}))
	os_type = forms.ModelChoiceField(queryset=OSType.objects.all(), widget=forms.Select(attrs={"class":"form-control", 'required':True}))
'''