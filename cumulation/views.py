from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.template import loader
from .forms import CountryForm
from cumulation.utils import create_country, process_states
from .models import Country
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
def index(request): 
	countries_list = Country.objects.filter(country_type="PR").order_by('name')
	template = loader.get_template('cumulation/index.html')
	context = {
		'countries_list': countries_list,
	}
	return HttpResponse(template.render(context, request))


def country_list(request):
	countries_list = Country.objects.filter(country_type="PR").order_by('name')
	paginator = Paginator(countries_list, 25)
	page = request.GET.get('page')
	countries = None
	try: 
		countries = paginator.page(page)
	except PageNotAnInteger: 
		countries = paginator.page(1)
	except EmptyPage: 
		countries = paginator.page(paginator.num_pages)

	template = loader.get_template('cumulation/country_list.html')
	context = {
		'countries': countries,
	}
	return HttpResponse(template.render(context, request))

def detail(request, country_id): 
	country = get_object_or_404(Country, pk=country_id)
	return render(request, 'cumulation/country_view.html', {'country': country})

def country_new(request):
	if request.method == "POST":
		form = CountryForm(request.POST)
		if form.is_valid(): 
			cleaned_data = form.cleaned_data
			print cleaned_data
			print "CREATING COUNTRY"
			country = create_country(cleaned_data)
			return render(request,  'cumulation/country_view.html', {'country': country})
	else: 

		form = CountryForm()
	return render(request, 'cumulation/country_edit.html', {'form': form})