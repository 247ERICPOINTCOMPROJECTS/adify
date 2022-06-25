from cProfile import label
from logging import PlaceHolder
from django import forms
from .models import Comments, Post
from tagify.fields import TagField
class NewPostForm(forms.ModelForm):

	class Meta:
		model = Post
		fields = ['title', 'description', 'pic', 'video', 'category', 'targetlocation', 'tags']
	def __init__(self, *args, **kwargs):
		super().__init__(*args,**kwargs)
		self.fields['tags'].set_tag_args('max_tags' , '5' )
	# def clean_tags(self):
	# 	tags = self.cleaned_data['tags']
	# 	tags = TagField(label='tag me ', place_holder="add tags ", delimiters=' ', max_tags=5)

		
	

class NewCommentForm(forms.ModelForm):

	class Meta:
		model = Comments
		fields = ['comment']