from django.db import models
# Create your models here.
from DjangoUeditor.models import UEditorField
class TestModel(models.Model):
    name = models.CharField(max_length=20,verbose_name='姓名')
    age = models.IntegerField(verbose_name='年龄')
    phone = models.CharField(max_length=11,verbose_name='手机')
    content = UEditorField(verbose_name='内容',
                           width=900,
                           height=600,
                           toolbars="full",
                           imagePath="media/ueditor/",
                           filePath="media/ueditor/",
                           upload_settings={"imageMaxSize":1204000},
                           default='')
    class Meta:
        verbose_name = '测试model'
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.name

class ForeginModel(models.Model):
    test_m = models.ForeignKey(TestModel,verbose_name='外键表')
    title = models.CharField(max_length=100,verbose_name='标题')
    add_time = models.DateTimeField(auto_now_add=True,verbose_name='添加日期')
    
    class Meta:
        verbose_name = '外键测试表'
        verbose_name_plural = verbose_name
    
