from django.forms import ModelForm
from .models import ProductPost

class ProductPostForm(ModelForm):
    '''ModelFormのサブクラス
    '''
    class Meta:
        '''ModelFormのインナークラス
        
        Attributes:
          model: モデルのクラス
          fields: フォームで使用するモデルのフィールドを指定
        '''
        model = ProductPost
        fields = ['category', 'title', 'comment', 'image1', 'image2']
