from django import forms



class UserBioForm(forms.Form):
    name = forms.CharField(label="Компания")
    email = forms.CharField(label="Email (для обратной связи)")
    topic = forms.CharField(label="Тема")
    text = forms.CharField(label="Сообщение", widget=forms.Textarea)

