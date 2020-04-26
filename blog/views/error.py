from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.http import Http404

def forbidden(request):
    return redirect('./post_list')

def handler404(request, exception, template_name="404.html"):
    response = render_to_response("404.html")
    response.status_code = 404
    return response

def get404(request):
    return render(request, '404.html')