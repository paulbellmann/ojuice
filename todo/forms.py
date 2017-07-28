from django import forms


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
    title = forms.CharField(max_length=285)
    title.widget.attrs = {
        'class': 'form-control add-todo',
        'placeholder': 'Add quick todo (Title Body)'
    }
