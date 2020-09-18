from django.db import models

# Create your models here.

class Customer(models.Model):
	MARITAL_STATUS=(
		('S','Single'),
		('M','Married'),
		('W','Widow/er'),
		('D','Divorced'),
	)
	NATURAL_GENDER=(
		('M','Male'),
		('F','Female'),
	)
	picture = models.ImageField()
	date_registered = models.DateField(auto_now_add=True)
	first_name = models.CharField(max_length=50)
	middle_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	street = models.CharField(max_length=50)
	brgy = models.CharField(max_length=50)
	city = models.CharField(max_length=50)
	province = models.CharField(max_length=50)
	zip_code = models.IntegerField()
	birthdate = models.DateField()
	status = models.CharField(max_length=1,choices=MARITAL_STATUS)
	gender = models.CharField(max_length=1,choices=NATURAL_GENDER)
	spouse_name = models.CharField(max_length=50)
	spouse_occupation = models.CharField(max_length=50)
	no_of_children = models.IntegerField()
	mother_name = models.CharField(max_length=50)
	mother_occupation = models.CharField(max_length=50)
	father_name = models.CharField(max_length=50)
	father_occupation = models.CharField(max_length=50)
	height = models.FloatField()
	weight = models.FloatField()
	religion = models.CharField(max_length=50)
	elementary_school = models.CharField(max_length=50)
	elementary_grade = models.CharField(max_length=50)
	elementary_year_completed = models.IntegerField()
	elementary_awards = models.TextField()
	junioir_high_school = models.CharField(max_length=50)
	junior_high_grade = models.CharField(max_length=50)
	junior_high_year_completed = models.IntegerField()
	junior_high_awards = models.TextField()
	senior_high_school = models.CharField(max_length=50)
	senior_high_grade = models.CharField(max_length=50)
	senior_high_year_completed = models.IntegerField()
	senior_high_awards = models.TextField()
	college_school = models.CharField(max_length=50)
	college_course = models.CharField(max_length=50)
	college_level = models.IntegerField()
	college_year_completed = models.IntegerField()
	college_awards = models.TextField()
	post_graduate_school = models.CharField(max_length=50)
	post_graduate_course = models.CharField(max_length=50)
	post_graduate_level = models.IntegerField()
	post_graduate_year_completed = models.IntegerField()
	post_graduate_awards = models.TextField()

	def __str__(self):
		return self.name

class Training(models.Model):
	title = models.CharField(max_length=50)
	sponsor = models.CharField(max_length=50)
	date = models.DateField()
	venue = models.CharField(max_length=50)
	customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

	class Meta:
		verbose_name = "Training"
		verbose_name_plural = "Trainings"

	def __str__(self):
		pass
    