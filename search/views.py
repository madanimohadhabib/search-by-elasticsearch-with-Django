from django.shortcuts import render
from .search import lookup


def search_view(request):
    query_params = request.GET
    q = query_params.get('q')

    context = {}

    if q is not None:
        results = lookup(q)
        context['results'] = results
        context['query'] = q
    return render(request, 'search.html', context)

