from django import forms
from . import models


class MessageForm(forms.ModelForm):
    class Meta:
        model = models.Message
        fields = '__all__'
        #fields = ('title','text',) برای وقتیکه میخای بگی فقط فلان و فلان فیلد رو ایمپوت کن
        #exclude = ['created']   وقتی که میخایم بگیم همه ی فیلدها باشد جز فلان فیلد
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your Title', 'style': 'width: 300px;'}),
            'text': forms.Textarea(attrs={'class': 'form-control'}),

        }