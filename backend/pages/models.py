from django.db import models
import uuid

# Create your models here.

#initialize table
class Person(models.Model):
	MARITAL_STATUS=[
		('S','Single'),
		('M','Married'),
		('W','Widow/er'),
		('D','Divorced'),
	]
	NATURAL_GENDER=[
		('M','Male'),
		('F','Female'),
	]
	first_name = models.CharField(max_length=50,default='',null=False)
	middle_name = models.CharField(max_length=50,default='',null=False)
	last_name = models.CharField(max_length=50,default='',null=False)
	street = models.CharField(max_length=50,default='',null=False)
	brgy = models.CharField(max_length=50,default='',null=False)
	city = models.CharField(max_length=50,default='',null=False)
	province = models.CharField(max_length=50,default='',null=False)
	country = models.CharField(max_length=50,default='',null=False)
	zip_code = models.IntegerField(default=0)
	birthdate = models.DateField()
	status = models.CharField(max_length=1,choices=MARITAL_STATUS,default='S',null=False)
	gender = models.CharField(max_length=1,choices=NATURAL_GENDER,default='M',null=False)
	spouse_name = models.CharField(max_length=50,default='',null=False)
	spouse_occupation = models.CharField(max_length=50,default='',null=False)
	no_of_children = models.IntegerField()
	mother_name = models.CharField(max_length=50,default='',null=False)
	mother_occupation = models.CharField(max_length=50,default='',null=False)
	father_name = models.CharField(max_length=50,default='',null=False)
	father_occupation = models.CharField(max_length=50,default='',null=False)
	height = models.FloatField(default=0)
	weight = models.FloatField(default=0)
	religion = models.CharField(max_length=50,default='',null=False)
	elementary_school = models.CharField(max_length=50,default='',null=False)
	elementary_grade = models.FloatField(default=1)
	elementary_year_completed = models.IntegerField(default=0)
	elementary_awards = models.TextField(default='',null=False)
	junioir_high_school = models.CharField(max_length=50,default='',null=False)
	junior_high_grade = models.FloatField(default=1)
	junior_high_year_completed = models.IntegerField(default=0)
	junior_high_awards = models.TextField(default='',null=False)
	senior_high_school = models.CharField(max_length=50,default='',null=False)
	senior_high_grade = models.FloatField(default=1)
	senior_high_year_completed = models.IntegerField(default=0)
	senior_high_awards = models.TextField(default='',null=False)
	college_school = models.CharField(max_length=50,default='',null=False)
	college_course = models.CharField(max_length=50,default='',null=False)
	college_level = models.IntegerField(default=0)
	college_year_completed = models.IntegerField(default=0)
	college_awards = models.TextField(default='',null=False)
	post_graduate_school = models.CharField(max_length=50,default='',null=False)
	post_graduate_course = models.CharField(max_length=50,default='',null=False)
	post_graduate_level = models.IntegerField(default=0)
	post_graduate_year_completed = models.IntegerField(default=0)
	post_graduate_awards = models.TextField(default='',null=False)

	class Meta:
		verbose_name = "Person"
		verbose_name_plural = "Persons"

	def __str__(self):
		return self.first_name

	def status_verbose(self):
		return dict(Person.MARITAL_STATUS)[self.status]

	def gender_verbose(self):
		return dict(Person.NATURAL_GENDER)[self.gender]

class Customer(Person):
	picture = models.ImageField()
	date_registered = models.DateField(auto_now_add=True)

	class Meta:
		verbose_name = "Customer"
		verbose_name_plural = "Customers"

	def __str__(self):
		return self.first_name

class Training(models.Model):
	title = models.CharField(max_length=50,default='',null=False)
	sponsor = models.CharField(max_length=50,default='',null=False)
	date = models.DateField()
	venue = models.CharField(max_length=50,default='',null=False)
	customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

	class Meta:
		verbose_name = "Training"
		verbose_name_plural = "Trainings"

	def __str__(self):
		pass
	
class Product(models.Model):
	date_registered = models.DateField(auto_now_add=True)
	category = models.CharField(max_length=30,null = False)
	pname = models.CharField(max_length=30,null = False)
	brand = models.CharField(max_length=30,null = False)
	color = models.CharField(max_length=30,null = False)
	size = models.CharField(max_length=30,null = False)
	price = models.FloatField(default=0)
	stock = models.IntegerField(default=0)
	image1 = models.ImageField()
	image2 = models.ImageField()
	image3 = models.ImageField()

	class Meta:
		verbose_name = "Product"
		verbose_name_plural = "Products"

	def __str__(self):
		return self.pname

class Order(models.Model):
	date_registered = models.DateField(auto_now_add=True)
	address = models.CharField(max_length=30,null = False)
	contact_number = models.CharField(max_length=11,null = False)
	email = models.CharField(max_length=30,null = False)
	customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
	product = models.ForeignKey(Product, on_delete=models.CASCADE)
	quantity = models.IntegerField(default=0)

	class Meta:
		verbose_name = "Order"
		verbose_name_plural = "Orders"
