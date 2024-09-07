from django.shortcuts import render
import requests
from .models import Quote
from .forms import QuoteSearchForm
from .utils import get_quote_of_the_day



# quotes/views.py

from django.shortcuts import render
from .utils import get_quote_of_the_day

def quote_of_the_day_view(request):
    # Get a random quote from the API
    quote_data = get_quote_of_the_day()
    return render(request, 'quotes.html', {'quote': quote_data['quote'], 'author': quote_data['author']})
