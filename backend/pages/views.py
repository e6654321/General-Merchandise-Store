from django.shortcuts import render, redirect
from django.views.generic import View, TemplateView
from .models import Customer
from .models import Product
from .models import Order
from .forms import CustomerCreate, ProductCreate, OrderCreate
from django.http import HttpResponse
from django.conf import settings

# Create your views here.
class HomePageView(TemplateView):
	def get(self, request):
		products = Product.objects.all()
		return render(request, 'index.html', {'isValid': -1, 'products': products})

	def post(self, request):
		products = Product.objects.all()
		form = OrderCreate(request.POST)
		if form.is_valid():
			customer_id=request.POST.get("customerId")
			address = request.POST.get("customerAddress")
			contact_number = request.POST.get("customerNumber")
			email = request.POST.get("customerEmail")
			fname = request.POST.get("customerName")
			product_id = request.POST.get("productName")
			quantity = request.POST.get("quantity")
			try:
				customer = Customer.objects.get(first_name=fname,person_ptr_id=customer_id)
				product = Product.objects.get(id=product_id)
				new_stock = product.stock - int(quantity)

				if(new_stock<0):
					raise Exception
					
				update_product = Product.objects.filter(id = product_id).update(stock=new_stock)
				form = Order(
							address=address,
							contact_number=contact_number,
							email=email,
							customer=customer,
							product=product,
							quantity=quantity
							)
				form.save()
				return render(request, 'index.html', {'isValid': 1, 'products': products})
			except Exception as e:
				print(e)
				return render(request, 'index.html', {'isValid': 0, 'products': products})
		else:
			print(form.errors)
			return HttpResponse('Not Valid')

class DashboardPageView(TemplateView):
	def get(self, request):
		total = 0
		all_orders = Order.objects.all()
		products_count = Product.objects.all().count()
		customers_count = Customer.objects.all().count()

		for order in all_orders:
			total += order.quantity * Product.objects.get(id=order.product_id).price

		total = int(total) if total==int(total) else total

		return render(request, 'dashboard.html', {'customers': customers_count, 'products': products_count, 'total': f'{total:,}'})

class LoginPageView(TemplateView):
	template_name = 'login.html'

#add new row in table db
class RegCustomerPageView(TemplateView):
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
							country=country,
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
			# customers = Customer.objects.all()
			# print(Customer.objects.get(id=1))
			# print(customers)
			return redirect('pages:tablecustomer')
		else:
			print(form.errors)
			return HttpResponse('Not Valid')

class RegProductPageView(TemplateView):
	def get(self,request):
		return render(request, 'regProduct.html')
	
	def post(self,request):
		form = ProductCreate(request.POST)
		if form.is_valid():
			pname = request.POST.get("productName")
			brand = request.POST.get("productBrand")
			color = request.POST.get("productColor")
			category = request.POST.get("productCategory")
			size = request.POST.get("productDimension")
			price = request.POST.get("productPrice")
			stock = request.POST.get("productStocks")
			image1 = request.POST.get("productImage1")
			image2 = request.POST.get("productImage2")
			image3 = request.POST.get("productImage3")

			form = Product(
				category = category,
				pname = pname,
				brand = brand,
				color = color,
				size = size,
				price = price,
				stock = stock,
				image1 = image1,
				image2 = image2,
				image3 = image3)
			form.save()
			# products = Product.objects.all()
			# return redirect(request, 'tableProduct.html', {'products': products})
			return redirect('pages:tableproduct')
		else:
			print(form.errors)
			return HttpResponse('Not Valid')

#get rows in table
class TableCustomerPageView(TemplateView):
	def get(self, request):
		customers = Customer.objects.all()
		return render(request, 'tableCustomer.html', {'customers': customers})

	def post(self, request):
		if 'btnUpdate' in request.POST:
			customer_id = request.POST.get("customer_id")
			fname = request.POST.get("customer_firstname")
			mname = request.POST.get("customer_middlename")
			lname = request.POST.get("customer_lastname")
			date = request.POST.get("customer_regdate")
			bdate = request.POST.get("customer_birthdate")
			customer_street = request.POST.get("customer_street")
			customer_brgy = request.POST.get("customer_brgy")
			customer_city = request.POST.get("customer_city")
			customer_province = request.POST.get("customer_province")
			customer_zip = request.POST.get("customer_zip")
			customer_country = request.POST.get("customer_country")
			customer_religion = request.POST.get("customer_religion")
			customer_gender = request.POST.get("customer_gender")
			customer_height = request.POST.get("customer_height")
			customer_status = request.POST.get("customer_status")
			customer_weight = request.POST.get("customer_weight")
			update_customer = Customer.objects.filter(id=customer_id).update(
							first_name=fname,
							middle_name=mname,
							last_name=lname,
							street=customer_street,
							brgy=customer_brgy,
							city=customer_city,
							province=customer_province,
							zip_code=customer_zip,
							birthdate=bdate,
							status=customer_status,
							gender=customer_gender,
							country=customer_country,
							religion=customer_religion,
							height=customer_height,
							weight=customer_weight,
							)
		elif 'btnDelete' in request.POST:
			customer_id = request.POST.get("customer_id")
			delete_customer = Customer.objects.filter(id = customer_id).delete()
			print('record deleted')
		# customers = Customer.objects.all()
		# return render(request, 'tableCustomer.html', {'customers': customers})
		return redirect('pages:tablecustomer')

class TableProductPageView(TemplateView):
	# template_name = 'tableProduct.html'
	def get(self, request):
		products = Product.objects.all()
		return render(request, 'tableProduct.html', {'products': products})

	def post(self, request):
		if 'btnUpdate' in request.POST:
			product_id = request.POST.get("product_id")
			pname = request.POST.get("product_name")
			category = request.POST.get("product_category")
			brand = request.POST.get("product_brand")
			color = request.POST.get("product_color")
			size = request.POST.get("product_size")
			price = request.POST.get("product_price")
			stock = request.POST.get("product_stock")
			update_product = Product.objects.filter(id = product_id).update(category = category,pname = pname,brand = brand,color = color,size = size,price = price,stock = stock)
		elif 'btnDelete' in request.POST:
			product_id = request.POST.get("product_id")
			delete_product = Product.objects.filter(id = product_id).delete()
			print('record deleted')
		# products = Product.objects.all()
		# return render(request, 'tableProduct.html', {'products': products})
		return redirect('pages:tableproduct')

class TableOrderPageView(TemplateView):
	# template_name = 'tableProduct.html'
	def get(self, request):
		orders = Order.objects.all()
		return render(request, 'tableOrder.html', {'orders': orders})

	def post(self, request):
		if 'btnDelete' in request.POST:
			order_id = request.POST.get("order_id")
			delete_order = Order.objects.filter(id = order_id).delete()
			print('record deleted')
		return redirect('pages:tableorder')

class ErrorPageView(TemplateView):
	template_name = '404.html'