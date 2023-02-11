from django import forms

from post.models import Post, Tag, Comment


class PostModelForm(forms.ModelForm):
    image = forms.ImageField(widget=forms.ClearableFileInput(attrs={'class': 'hidden'}))
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=forms.SelectMultiple(attrs={
            'class': 'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 '
                     'focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 '
                     'dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500',
            'required': False
        }))
    content = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'dark:bg-gray-700 mt-1  w-full rounded-md border-gray-300 shadow-sm pl-3'
                 'focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm dark:bg-gray-700 dark:border-gray-600 '
                 'dark:placeholder-gray-400 p-3 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500',
        'placeholder': 'Write your post content',
        'rows': 6,
        'id': 'content'}))

    title = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'dark:bg-gray-700 mt-1 block w-full rounded-md '
                 'border-gray-300 dark:text-white '
                 'shadow-sm focus:border-indigo-500 '
                 'focus:ring-indigo-500 sm:text-sm',
        'placeholder': 'Write a title...'
    }))

    class Meta:
        model = Post
        fields = ['image', 'title', 'tags', 'content']

    def __int__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        print(self.fields)


class CommentModelForm(forms.ModelForm):
    body = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'px-0 w-full text-sm text-gray-900 border-0 focus:ring-0 dark:text-white dark:placeholder-gray-400 '
                 'dark:bg-gray-800',
        'rows': 6,
        'placeholder': 'Write a comment...'}))

    class Meta:
        model = Comment
        fields = ['body', ]
