from django.db import models

# Create your models here.
class Message(models.Model):
	name = models.CharField(max_length = 50, blank = False)
	email = models.EmailField()
	subject = models.CharField(max_length = 50, blank = False)
	message = models.CharField(max_length = 1000, blank = False)

	def __str__(self):
		return self.subject

	class Meta():
		db_table = 'Reviews'

class Upload(models.Model):
	name = models.CharField(max_length = 50, blank = False)
	image = models.ImageField(default = "display/images.png")
	file = models.FileField(upload_to = 'pdfs/', null = False)

	def __str__(self):
		return self.name

	class Meta():
	 	db_table = 'Upload'

	def clean_name(self):
	 	return self.cleaned_data['name'].lower()

	def save(self, force_insert=False, force_update=False):
		self.name = self.name.lower()
		super(Upload, self).save(force_insert, force_update)