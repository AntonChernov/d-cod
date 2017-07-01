from django.shortcuts import render
from django.http import JsonResponse
from django.core.exceptions import ObjectDoesNotExist
from .models import DataSetModel


def return_charts(request):
    if request.method == 'GET':
        data_map = {}
        try:
            objects_set = DataSetModel.objects.all().distinct('group_region')
            if len(objects_set) > 1:
                data_map['error'] = False
            else:
                data_map['error'] = True
                data_map['message'] = 'DB is empty!'
        except ObjectDoesNotExist:
            data_map['error'] = True
            data_map['message'] = 'DB is empty!'
            objects_set = ''
        titles = [i.group_region for i in objects_set]
        data_map['title'] = titles
        counts_of_title = []
        series_to_chart = []
        for title in titles:
            data = DataSetModel.objects.filter(group_region=title)
            counter = data.count()
            counts_of_title.append({'name': title, 'y': counter, 'drilldown': title})
        object_set = DataSetModel.objects.filter(group_region=request.GET.get('region'))
        for i in object_set:
            series_to_chart.append({'name': i.parameter_country, 'y': int(i.value), 'drilldown': i.parameter_country})
        data_map['series_chart'] = series_to_chart
        data_map['count'] = counts_of_title
        return JsonResponse(data=data_map, safe=False, content_type="application/json")


def return_empty_page(request):
    data_map = {}
    try:
        objects_set = DataSetModel.objects.all().distinct('group_region')
        if len(objects_set) > 1:
            data_map['error'] = False
            data_map['region'] = objects_set
            return render(request, 'main.html', {'data': data_map})
        else:
            data_map['error'] = True
            data_map['message'] = 'DB is empty!'
    except ObjectDoesNotExist:
        data_map['error'] = True
        data_map['message'] = 'DB is empty!'
        objects_set = ''
    return render(request, 'main.html')

