import xadmin  
from xadmin import views  
from .models import VerifyCode  
  
  
class BaseSetting(object):  
    enable_themes = True  
    use_bootswatch = True  
  
  
class GlobalSettings(object):  
    site_title = "backend"  
    site_footer = "vueshop"  
    # menu_style = "accordion"  
  
  
class VerifyCodeAdmin(object):  
    list_display = ['code', 'mobile', "add_time"]  