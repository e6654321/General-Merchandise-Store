from django.shortcuts import render
from django.views.generic import View, TemplateView
from .models import Customer
from .forms import CustomerCreate
from django.http import HttpResponse

# Create your views here.
class HomePageView(TemplateView):
    template_name = 'index.html'

class DashboardPageView(TemplateView):
    template_name = 'dashboard.html'

class LoginPageView(TemplateView):
    template_name = 'login.html'

#add new row in table db
class RegCustomerPageView(View):
    def get(self, request):
    	return render(request, 'regCustomer.html')

    def post(self, request):
    	form = CustomerCreate(request.POST)
    	if form.is_valid():
    		picture = request.POST.get("profile-picture")
    		fname = request.POST.get("firstname")
    		mname = request.POST.get("middlename")
    		lname = request.POST.get("lastname")
    		street = request.POST.get("street")
    		brgy = request.POST.get("barangay")
    		city = request.POST.get("city")
    		prov = request.POST.get("province")
    		zipcode = 0 if not request.POST.get("zip").isnumeric() else request.POST.get("zip")
    		country = request.POST.get("country")
    		religion = request.POST.get("religion")
    		gender = request.POST.get("gender")
    		birthdate = '2000-01-01' if request.POST.get("birthdate")=='' else request.POST.get("birthdate")
    		status = request.POST.get("status")
    		height = 1 if request.POST.get("height")=='' else request.POST.get("height")
    		weight = 1 if request.POST.get("weight")=='' else request.POST.get("weight")
    		spousename = request.POST.get("spousefname") + request.POST.get("spousemname") + request.POST.get("spouselname")
    		spouseocc = request.POST.get("spouseocc")
    		children = 0 if not request.POST.get("children").isnumeric() else request.POST.get("children")
    		mothername = request.POST.get("motherfname") + request.POST.get("mothermname") + request.POST.get("motherlname")
    		motherocc = request.POST.get("motherocc")
    		fathername = request.POST.get("fatherfname") + request.POST.get("fathermname") + request.POST.get("fatherlname")
    		fatherocc = request.POST.get("fatherocc")
    		elemschool = request.POST.get("elemschool")
    		elemgrade = 1 if request.POST.get("elemgrade")=='' else request.POST.get("elemgrade")
    		elemyear = 0 if not request.POST.get("elemyear").isnumeric() else request.POST.get("elemyear")
    		elemawards = request.POST.get("elemawards")
    		jhschool = request.POST.get("jhschool")
    		jhgrade = 1 if request.POST.get("jhgrade")=='' else request.POST.get("jhgrade")
    		jhyear = 0 if not request.POST.get("jhyear").isnumeric() else request.POST.get("jhyear")
    		jhawards = request.POST.get("jhawards")
    		shschool = request.POST.get("shschool")
    		shgrade = 1 if request.POST.get("shgrade")=='' else request.POST.get("shgrade")
    		shyear = 0 if not request.POST.get("shyear").isnumeric() else request.POST.get("shyear")
    		shawards = request.POST.get("shawards")
    		shstrand = request.POST.get("shstrand")
    		clgschool = request.POST.get("clgschool")
    		clgcourse = request.POST.get("clgcourse")
    		clglevel = 1 if not request.POST.get("clglevel").isnumeric() else request.POST.get("clglevel")
    		clgyear = 0 if not request.POST.get("clgyear").isnumeric() else request.POST.get("clgyear")
    		clgawards = request.POST.get("clgawards")
    		pgschool = request.POST.get("pgschool")
    		pgcourse = request.POST.get("pgcourse")
    		pglevel = 1 if not request.POST.get("pglevel").isnumeric() else request.POST.get("pglevel")
    		pgyear = 0 if not request.POST.get("pgyear").isnumeric() else request.POST.get("pgyear")
    		pgawards = request.POST.get("pgawards")
    		print(height)
    		form = Customer(picture=picture, 
    						first_name=fname,
    						middle_name=mname,
    						last_name=lname,
    						street=street,
    						brgy=brgy,
    						city=city,
    						province=prov,
    						zip_code=zipcode,
    						birthdate=birthdate,
    						status=status,
    						gender=gender,
    						spouse_name=spousename,
    						spouse_occupation=spouseocc,
    						no_of_children=children,
    						mother_name=mothername,
    						mother_occupation=motherocc,
    						father_name=fathername,
    						father_occupation=fatherocc,
    						height=height,
    						weight=weight,
    						religion=religion,
    						elementary_school=elemschool,
    						elementary_grade=elemgrade,
    						elementary_year_completed=elemyear,
    						elementary_awards=elemawards,
    						junioir_high_school=jhschool,
    						junior_high_grade=jhgrade,
    						junior_high_year_completed=jhyear,
    						junior_high_awards=jhawards,
    						senior_high_school=shschool,
    						senior_high_grade=shgrade,
    						senior_high_year_completed=shyear,
    						senior_high_awards=shawards,
    						college_school=clgschool,
    						college_course=clgcourse,
    						college_level=clglevel,
    						college_year_completed=clgyear,
    						college_awards=clgawards,
    						post_graduate_school=pgschool,
    						post_graduate_course=pgcourse,
    						post_graduate_level=pglevel,
    						post_graduate_year_completed=pgyear,
    						post_graduate_awards=pgawards)
    		form.save()
    		return HttpResponse('Customer record saved!')
    	else:
    		print(form.errors)
    		return HttpResponse('Not Valid')

class RegProductPageView(TemplateView):
    template_name = 'regProduct.html'

#get rows in table
class TableCustomerPageView(TemplateView):
	def get(self, request):
		customers = Customer.objects.all()
		return render(request, 'tableCustomer.html', {'customers': customers})

class TableProductPageView(TemplateView):
    template_name = 'tableProduct.html'

class ErrorPageView(TemplateView):
    template_name = '404.html'

#not yet implemented
def update_customer(request, customer_id):
	customer_id = int(customer_id)
	try:
		customer_sel = Customer.objects.get(id = customer_id)
	except Customer.DoesNotExist:
		return redirect('regcustomer')
	customer_form = CustomerCreate(request.POST or None, instance = customer_sel)
	if customer_form.is_valid():
		customer_form.save()
		return redirect('regcustomer')
	return render(request, 'pages/tableCustomer.html', {'upload_form':customer_form})

def delete_customer(request, customer_id):
	customer_id = int(customer_id)
	try:
		customer_sel = Customer.objects.get(id = customer_id)
	except Customer.DoesNotExist:
		return redirect('regcustomer')
	customer_sel.delete()
	return redirect('regcustomer')