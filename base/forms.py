from django import forms
from . models import Department,PositionList,EmpList

class dep_reg(forms.ModelForm):
    class Meta:
        model =Department
        fields = '__all__'

class position_reg(forms.ModelForm):
    class Meta:
        model = PositionList
        fields = '__all__'

class emp_reg(forms.ModelForm):
    class Meta:
        model = EmpList
        fields = '__all__'