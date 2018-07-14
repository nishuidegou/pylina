from django.shortcuts import render


import tushare as ts


# Create your views here.
def stock(request):

    # df = ts.get_realtime_quotes(['600848','000980','000981'])
    df = ts.get_stock_basics()

    _context = {
        'df': df.to_html()
    }

    return render(request, 'stock/stock_index.html', _context)