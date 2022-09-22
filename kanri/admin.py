from django.contrib import admin

# Register your models here.

# CustomUserをインポート
from .models import Category, ProductPost

class CategoryAdmin(admin.ModelAdmin):
  '''管理ページのレコード一覧に表示するカラムを設定するクラス
  
  '''
  # レコード一覧にidとtitleを表示
  list_display = ('id', 'title')
  # 表示するカラムにリンクを設定
  list_display_links = ('id', 'title')

class ProductPostAdmin(admin.ModelAdmin):
  '''管理ページのレコード一覧に表示するカラムを設定するクラス
  
  '''
  # レコード一覧にidとtitleを表示
  list_display = ('id', 'title')
  # 表示するカラムにリンクを設定
  list_display_links = ('id', 'title')

# Django管理サイトにCategory、CategoryAdminを登録する
admin.site.register(Category, CategoryAdmin)

# Django管理サイトにPhotoPost、PhotoPostAdminを登録する
admin.site.register(ProductPost, ProductPostAdmin)