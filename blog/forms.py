from django import forms
from .models import comment


class commentForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.author = kwargs.pop("author", None)
        self.post = kwargs.pop("post", None)
        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        comment = super().save(commit=False)
        comment.author = self.author
        comment.post = self.post
        comment.save()

    class Meta:
        model = comment
        fields = ["body"]
