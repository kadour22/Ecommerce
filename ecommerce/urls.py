from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path , include
from debug_toolbar.toolbar import debug_toolbar_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Category/', include('Category.urls')),
    path('Customer/', include('Customer.urls')),
    path('Product/', include('Product.urls')),
    path('CartItems/', include('CartItems.urls')),
    path('Order/', include('Order.urls')),
    path('__debug__/', include('debug_toolbar.urls'),name="toolbar"),
] 

urlpatterns += static(settings.MEDIA_URL , document_root = settings.MEDIA_ROOT)
