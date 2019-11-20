from django.db import models

# Create your models here.
class ChirpItem(models.Model):
	text = models.CharField(max_length=128)
	# chirp_id = models.IntegerField(primary_key=True)
