from django.shortcuts import render, get_object_or_404
from .models import Research
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


@login_required
def topic_view(request, id):
    research_object = get_object_or_404(Research, pk = id)
    node = research_object
    while node.parent is not None:
        node = node.parent
    data = node
    
    return render(request, 'Data/graph.html', {'research_object': research_object, 'Ancestor': data})

@login_required
def Red(request):
    research_object = Research.objects.first()
    return render(request, 'Data/graph.html', {'research_object': research_object, 'Ancestor': research_object})

@login_required
def Index(request):
    results = Research.objects.all()
    paginator = Paginator(results, 25)
    page_number = request.GET.get('page')
    context = {}
    try:
        context['page_obj'] = paginator.page(page_number)
    except PageNotAnInteger:
        context['page_obj'] = paginator.page(1)
    except EmptyPage:
        context['page_obj'] = paginator.page(paginator.num_pages)
    return render(request, 'Data/Index.html', context)

@login_required
def Search(request):
    search_phrase = request.GET.get('search')
    if search_phrase is not None:
        results = Research.objects.filter(level__lt = 3).filter(title__icontains = search_phrase)
        context = {}
        context['search_phrase'] = search_phrase
        paginator = Paginator(results, 25)
        page_number = request.GET.get('page')
        try:
            context['page_obj'] = paginator.page(page_number)
        except PageNotAnInteger:
            context['page_obj'] = paginator.page(1)
        except EmptyPage:
            context['page_obj'] = paginator.page(paginator.num_pages)

        return render(request, 'Data/Index.html', context)
    return render(request, 'Data/Index.html', {'search_phrase': search_phrase})