from django import forms
from .models import Jasoseol

class JssForm(forms.ModelForm):

    class Meta:
        model = Jasoseol
        fields = ('title', 'content',)
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # super - 부모 클래스에서 가져와서 쓸 수 있다.
        self.fields['title'].label = '제목'
        self.fields['content'].label = '자기소개서 내용'    
        self.fields['title'].widget.attrs.update(
            {
                'class': 'jss_title',
                'placeholder': '제목',
            }
        )