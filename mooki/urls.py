from django.contrib import admin
from django.urls import path, include
from blog import views
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import handler400, handler403, handler404, handler500

urlpatterns = [
    path('', include('blog.urls')),
    path('blog/', include('blog.urls')),
    path('d5gs4q8q93v4f/', admin.site.urls, name='admin_site'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler400 = 'blog.views.bad_request'
handler403 = 'blog.views.permission_denied'
handler404 = 'blog.views.page_not_found'
handler500 = 'blog.views.server_error'
