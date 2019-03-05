from django import forms

from .models import Post
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class JoinForm(UserCreationForm):
    username = forms.CharField(required = True)
    email = forms.EmailField(required = True)

    class Meta:
        model = User
        fields = ('username','email','password1','password2')

    def save(self, commit=True):
        user = super(JoinForm,self).save(commit=True)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user


class PostForm(forms.ModelForm):
    title = forms.CharField()
    text = forms.CharField(widget=forms.Textarea(
            attrs={
            'placeholder': '내용',
            "rows":8,}
    ))

    class Meta:
        model = Post
        fields = ['title', 'text','image']


    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        self.fields['image'].required = False