from django import forms

class BlogsForm(forms.Form):
    tag=forms.CharField()
    innerHTML1=forms.CharField(required=False)
    innerHTML2= forms.CharField(required=False)
    img=forms.ImageField(required=False)


class BlogsTitleForm(forms.Form):
    title=forms.CharField()

class BlogIdForm(forms.Form):
    blogId = forms.IntegerField()

class GenreForm(forms.Form):
    genre=forms.CharField()