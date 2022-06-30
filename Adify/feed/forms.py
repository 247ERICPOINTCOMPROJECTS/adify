from cProfile import label
from logging import PlaceHolder
from tkinter import Widget
from django import forms
from .models import Comments, Post
from tagify.fields import TagField
from django.forms.widgets import FileInput



class NewPostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ['title', 'description','pic', 'video', 'category', 'targetlocation', 'tags']


	def __init__(self, *args, **kwargs):
		super().__init__(*args,**kwargs)
		self.fields['tags'].set_tag_args('max_tags' , '5' )


# 1- edit post button update 
# 5- my profile


	

class NewCommentForm(forms.ModelForm):

	class Meta:
		model = Comments
		fields = ['comment']