from django.shortcuts import render, render_to_response
import pandas

# Create your views here.
from swallows_app.models import BattingStat

cols = [
    'f_name', 'l_name', 'age', 'g', 'pa',
    'ab', 'r', 'h', '_2b', '_3b', 'hr',
    'rbi', 'sb', 'cs', 'bb', 'so', 'ba',
    'obp', 'slg', 'ops', 'tb', 'gdp',
    'hbp', 'sh', 'sf', 'ibb'
]

def index(request):
    cols = [
        'f_name', 'l_name', 'age', 'g', 'pa',
        'ab', 'r', 'h', '_2b', '_3b', 'hr',
        'rbi', 'sb', 'cs', 'bb', 'so', 'ba',
        'obp', 'slg', 'ops', 'tb', 'gdp',
        'hbp', 'sh', 'sf', 'ibb'
    ]

    all_players = pandas.DataFrame.from_records(BattingStat.objects.all().values())
    all_players = all_players.reindex(columns=cols)
    return render_to_response('index.html', {'players': all_players.to_html(escape=False, index=False,
                                                                            justify='center', bold_rows=False)})
