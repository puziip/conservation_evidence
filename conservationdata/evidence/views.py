from django.http import JsonResponse
from django.db.models import Avg
from .models import Evidence


def average_score_by_species(request):
    data = (
        Evidence.objects
        .values('species_group')
        .annotate(avg_score=Avg('effectiveness_score'))
    )
    return JsonResponse(list(data), safe=False)


def high_effectiveness_interventions(request):
    interventions = (
        Evidence.objects
        .filter(effectiveness_score__gt=4)
        .values('intervention_title', 'effectiveness_score')
    )
    return JsonResponse(list(interventions), safe=False)
