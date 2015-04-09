from django.shortcuts import render_to_response,get_object_or_404
from .models import article
# Create your views here.
def subject(request):
	articles=article.objects.filter(published_data__isnull=False).order_by('published_data')
	return render_to_response('subject.html',{'articles':articles})

def detail(request,pk):
	post = get_object_or_404(article, pk=pk)
	return render_to_response('detail.html',{'post':post})

def about(request):
	return render_to_response('about.html',{})
