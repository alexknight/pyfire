from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class article(models.Model):
	author = models.ForeignKey(User)
	title = models.CharField(max_length=200)
	text = models.TextField()
	created_date = models.DateTimeField(default=timezone.now)
	published_data = models.DateTimeField(blank=True,null=True)

	def publish(self):
		self.published_date = timezone.now()

	def __unicode__(self):
		return self.title