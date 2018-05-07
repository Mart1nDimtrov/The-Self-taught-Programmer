from django.db import models

class Custmer(models.Model):
	username = models.CharField()

user1 = Customer.objects.create(username="eddie")
eddie = Customer.objects.get(username="eddie")
print(eddie)