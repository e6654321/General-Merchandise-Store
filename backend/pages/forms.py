from django import forms
from .models import *
#DataFlair

#form for all data in table
class CustomerCreate(forms.ModelForm):
	picture = forms.ImageField(required=False)
	date_registered = forms.DateField(required=False)
	first_name = forms.CharField(required=False)
	middle_name = forms.CharField(required=False)
	last_name = forms.CharField(required=False)
	street = forms.CharField(required=False)
	brgy = forms.CharField(required=False)
	city = forms.CharField(required=False)
	province = forms.CharField(required=False)
	country = forms.CharField(required=False)
	zip_code = forms.IntegerField(required=False)
	birthdate = forms.DateField(required=False)
	status = forms.CharField(required=False)
	gender = forms.CharField(required=False)
	spouse_name = forms.CharField(required=False)
	spouse_occupation = forms.CharField(required=False)
	no_of_children = forms.IntegerField(required=False)
	mother_name = forms.CharField(required=False)
	mother_occupation = forms.CharField(required=False)
	father_name = forms.CharField(required=False)
	father_occupation = forms.CharField(required=False)
	height = forms.FloatField(required=False)
	weight = forms.FloatField(required=False)
	religion = forms.CharField(required=False)
	elementary_school = forms.CharField(required=False)
	elementary_grade = forms.FloatField(required=False)
	elementary_year_completed = forms.IntegerField(required=False)
	elementary_awards = forms.CharField(required=False)
	junioir_high_school = forms.CharField(required=False)
	junior_high_grade = forms.FloatField(required=False)
	junior_high_year_completed = forms.IntegerField(required=False)
	junior_high_awards = forms.CharField(required=False)
	senior_high_school = forms.CharField(required=False)
	senior_high_grade = forms.FloatField(required=False)
	senior_high_year_completed = forms.IntegerField(required=False)
	senior_high_awards = forms.CharField(required=False)
	college_school = forms.CharField(required=False)
	college_course = forms.CharField(required=False)
	college_level = forms.IntegerField(required=False)
	college_year_completed = forms.IntegerField(required=False)
	college_awards = forms.CharField(required=False)
	post_graduate_school = forms.CharField(required=False)
	post_graduate_course = forms.CharField(required=False)
	post_graduate_level = forms.IntegerField(required=False)
	post_graduate_year_completed = forms.IntegerField(required=False)
	post_graduate_awards = forms.CharField(required=False)
	class Meta:
		model = Customer
		fields = '__all__'

class ProductCreate(forms.ModelForm):
	date_registered = forms.DateField(required=False)
	category = forms.CharField(required = False)
	pname = forms.CharField(required = False)
	brand = forms.CharField(required = False)
	color =forms.CharField(required = False)
	size =forms.CharField(required = False)
	price = forms.FloatField(required = False)
	stock = forms.IntegerField(required = False)
	image1 = forms.ImageField(required = False)
	image2 = forms.ImageField(required = False)
	image3 = forms.ImageField(required = False)
	class Meta:
		model = Product
		fields = '__all__'