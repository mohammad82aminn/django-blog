from dataclasses import field

from django import forms
from .models import Comment, Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            "title", 
            "text",
        ]

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = [
            'name',
            'email',
            'text'
        ]
        
        widgets = {

                    "name": forms.TextInput(
                        attrs={
                            "class": "form-control",
                            "placeholder": "Your name",
                        }
                    ),


                    "email": forms.EmailInput(
                        attrs={
                            "class": "form-control",
                            "placeholder": "Your email",
                        }
                    ),


                    "text": forms.Textarea(
                        attrs={
                            "class": "form-control",
                            "placeholder": "Write your comment...",
                            "rows": 4,
                        }
                    ),

                }