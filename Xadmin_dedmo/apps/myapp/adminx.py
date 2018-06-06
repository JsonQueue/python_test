import xadmin
from xadmin import views


from .models import TestModel,ForeginModel


# 添加ueditor插件
# 由于已经将xadmin源文件拷贝到了项目下，为extra_apps/xadmin，在xadmin下的plugin中新建一个ueditor.py文件




# 全局内容配置,头部系统名,底部版权管理器,折叠表
class GloableSettings(object):
    
    site_title = '智游后台管理系统' #头部系统名
    site_footer = '智游后台管理系统, 智游教育版权所有' # 底部版权
    menu_style = 'accordion' # 设置数据库管理导航折叠,一个app为一个折叠框

# 注册
xadmin.site.register(views.CommAdminView,GloableSettings)

from django.contrib import admin

# 主题配置
class BaseSetging(object):
    enable_themes = True # 使用主题
    use_bootswatch = True #

xadmin.site.register(views.BaseAdminView,BaseSetging) # 将主题管理器绑定


class CustomAdmin(object):
    # 设置xadmin后台显示字段
    list_display = ['name','age','phone','content']
    # 设置xadmin后台搜索字段,注意:搜索字段不能有时间类型,否则会报错
    search_fields = ['name','age','phone','content']
    # 设置xadmin后台过滤器筛选字段,时间字段可以用过滤器做
    list_filter =  ['age']
    # 设置可以在列表直接修改的字段
    list_editable = ['name','age']
    # 设置自动刷新
    refresh_times = [5,7]
    # 配置插件效果
    style_fields = {'content':'ueditor'}
    
    
    

# 将数据表注册到xadmin后台显示
xadmin.site.register(TestModel,CustomAdmin)


class ForeginAdmin(object):
    list_display = ['title','test_m','add_time']
    # test_m__name 表示通过test_m外键字段查询关联表中的name字段
    search_fields = ['title','test_m__name']
    list_filter = ['test_m__name','add_time']
    
    ordering = ['-add_time']
    readonly_fields = ['title']
    
xadmin.site.register(ForeginModel,ForeginAdmin)