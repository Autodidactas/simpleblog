from django.db import models
from django.contrib.auth.models import User
from tagging_autocomplete.models import TagAutocompleteField
import os

# Create your models here.

class Categoria(models.Model):
	nombre = models.CharField(max_length=200)

	def __unicode__(self):
		return self.nombre

class Posts(models.Model):
	fecha = models.DateField()
	titulo = models.CharField(max_length=200)
	slug = models.CharField(max_length=200)
	contenido = models.TextField()
	autor = models.ForeignKey(User)
	categoria = models.ForeignKey(Categoria)
	tag = TagAutocompleteField('Tags', help_text='Separa con coma(,)',
		                       null=True,blank=True)


	def __unicode__(self):
		return self.titulo

	def adjunto(self):
		adjunto = Archivos.objects.filter(fk_post__id=self.id)
		return adjunto

	def get_absolute_url(self):
		return '/blog/%s/' % (self.slug)

	class Meta:
		verbose_name=u'Post'

def get_file_path(intance,filename):
	return os.path.join(intance.fileDir, filename)

class Archivos(models.Model):
	nombre = models.CharField(max_length=200)
	archivo = models.FileField(upload_to=get_file_path)

	fk_post = models.ForeignKey(Posts)
	fileDir = 'archivos/'

	def __unicode__(self):
		return self.nombre

	class Meta:
		verbose_name=u'Subir archivos'
