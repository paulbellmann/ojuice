from django import forms

class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)
    your_pass = forms.CharField(label='Password', min_length=1)
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.PasswordInput)
    sender = forms.EmailField()
    cc_myself = forms.BooleanField(required=False)

class TodoForm(forms.Form):
    title = forms.CharField(max_length=30)
    title.widget.attrs = {
        'class': 'form-control',
        'placeholder': 'Homework',
        'aria-describedby': 'basic-addon1'
    }
    body = forms.CharField(widget=forms.Textarea, max_length=255)
    body.widget.attrs = {
        'class': 'form-control',
        'placeholder': 'Page 1337',
        'rows': '5'
    }

class QuickTodoForm(forms.Form):
    title = forms.CharField(max_length=30)
    title.widget.attrs = {
        'class': 'form-control add-todo',
        'placeholder': 'Add quick todo (#Title Body)'
    }