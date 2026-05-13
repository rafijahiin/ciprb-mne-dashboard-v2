import json
from django.shortcuts import render
from django.db.models import Count
from tracker.models import FistulaCase
from mpdsr.models import MPDSREvent


def dashboard_main(request):
    fistula_operated = FistulaCase.objects.filter(referral_status='OPERATED').count()
    fistula_goal = 100
    fistula_progress = (fistula_operated / fistula_goal * 100) if fistula_goal > 0 else 0

    mpdsr_districts = MPDSREvent.objects.values('district').annotate(death_count=Count('event_id')).order_by('-death_count')
    heatmap_labels = json.dumps([item['district'] for item in mpdsr_districts])
    heatmap_data = json.dumps([item['death_count'] for item in mpdsr_districts])

    total_mpdsr = MPDSREvent.objects.count()
    implemented_mpdsr = MPDSREvent.objects.filter(action_status='IMPLEMENTED').count()
    action_gap_percent = (implemented_mpdsr / total_mpdsr * 100) if total_mpdsr > 0 else 0

    mpdsr_events = MPDSREvent.objects.all().order_by('-event_id')

    context = {
        'fistula_operated': fistula_operated,
        'fistula_goal': fistula_goal,
        'fistula_progress': fistula_progress,
        'heatmap_labels': heatmap_labels,
        'heatmap_data': heatmap_data,
        'action_gap_percent': action_gap_percent,
        'mpdsr_events': mpdsr_events,
    }
    return render(request, 'dashboard/main.html', context)
