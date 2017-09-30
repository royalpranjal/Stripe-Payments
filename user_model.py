from django.db import models

class User(models.Model):
  stripe_id = models.CharField(max_length=255, blank=True, null=True)
  email = models.CharField(max_length=255)
  
  # It's just a sample model. Create your own according to the needs of the project.
