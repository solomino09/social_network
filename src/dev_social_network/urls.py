from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path(
        'dev/',
        include('pages.urls', namespace='pages')
    ),
    path(
        'accounts/',
        include('accounts.urls', namespace='accounts')
    ),
    path(
        'posts/',
        include('posts.urls', namespace='posts')
    ),
    path(
        'posts/',
        include('likes.urls', namespace='likes')
    ),
    path(
        'posts/',
        include('unlikes.urls', namespace='unlikes')
    ),
    path(
        'posts/',
        include('comments.urls', namespace='comments')
    ),
    path(
        '',
        RedirectView.as_view(url='posts/', permanent=True)
    ),
    path('admin/', admin.site.urls),
]


if settings.DEBUG:
    from django.conf.urls.static import static

    urlpatterns += static(
        settings.STATIC_URL,
        document_root=settings.STATIC_ROOT
    )
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )
