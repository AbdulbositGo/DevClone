from django import forms

from post.models import Post, Tag, Comment


text_input_class = 'border border-gray-300 text-black font-semibold text-sm rounded-lg w-full p-2.5 ' \
                   'focus:ring-purple-700 focus:border-purple-700 dark:bg-black dark:border-zinc-700 ' \
                   'dark:placeholder-gray-400 dark:hover:border-zinc-600 dark:text-white'


class PostModelForm(forms.ModelForm):
    image = forms.ImageField(widget=forms.ClearableFileInput(attrs={'class': 'hidden'}))
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=forms.SelectMultiple(attrs={
            'class': text_input_class,
            'required': False
        }))
    content = forms.CharField(widget=forms.Textarea(attrs={
        'class': text_input_class, 'placeholder': 'Write your post content','rows': 6,'id': 'content'
    }))

    title = forms.CharField(widget=forms.TextInput(attrs={
        'class': text_input_class, 'placeholder': 'Write a title...'
    }))

    class Meta:
        model = Post
        fields = ['image', 'title', 'tags', 'content']

    def __int__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        print(self.fields)


class CommentModelForm(forms.ModelForm):
    body = forms.CharField(required=True, label='comment', widget=forms.Textarea(attrs={
        'class': 'px-0 w-full text-sm text-gray-900 border-0 focus:ring-0 dark:text-white dark:placeholder-gray-400 '
                 'dark:bg-gray-800',
        'rows': 6,
        'placeholder': 'Write a comment...'}))

    class Meta:
        model = Comment
        fields = ['body', ]
