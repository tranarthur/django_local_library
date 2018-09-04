"""locallibrary URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
# Use include() to add paths from the catalog application 
from django.conf.urls import include
#Add URL maps to redirect the base URL to our application
from django.views.generic import RedirectView
# Use static() to add url mapping to serve static files during development (only)
from django.conf import settings
from django.conf.urls.static import static
""" 
There are a number of ways to extend the urlpatterns list 
(above we just appended a new list item using the += operator 
to clearly separate the old and new code). 
We could have instead just included this new pattern-map 
in the original list definition
"""
urlpatterns = [
    path('admin/', admin.site.urls),
]

"""
add a new list item tothe urlpatterns list
this new item includes a path() that forwards requests with the pattern catalog/
to the module catalog.urls
"""
urlpatterns += [
    path('catalog/', include('catalog.urls')),
]
#redirect the root URL of our site to 127.0.0.1:8000/catalog/
urlpatterns += [
    path('', RedirectView.as_view(url='/catalog/')), 
]
"""
    RedirectView takes as its first argument the new relative URL to redirect to
    (/catalog/) when the URL pattern specified in the path() function is matched
    (the root URL, in this case).
    """

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
"""
Django does not serve static files by default 
 As a final addition to this URL mapper, 
 you can enable the serving of static files during development 
 by appending the following lines. 
"""
# Add Django site authentication urls (for login, logout, password management)
urlpatterns += [path('accounts/', include('django.contrib.auth.urls')),]