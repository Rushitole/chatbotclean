from django.db import models
from django.contrib.auth.models import User

# Create your models here.



class ChatMessage(models.Model):
	# user=models.ForeignKey(User,on_delete=models.CASCADE)
	user_message=models.TextField()
	bot_response=models.TextField()
	created_at=models.DateTimeField(auto_now=True)


def __str__(self):                            #readble string representation of an object (for djnago admin pannel)
	return self.user_message





