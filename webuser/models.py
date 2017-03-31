from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class WebUser(models.Model):
    user=models.OneToOneField(User)
    online = models.IntegerField(default=False)
    friends = models.ManyToManyField("self")
    sex = models.IntegerField(default=1)
    is_student = models.IntegerField(default=1)

    def __unicode__(self):
        return self.user.username

    def get_url(self):
        url = self.url
        if "http://" not in self.url and "https://" not in self.url and len(self.url)>0:
            url ="http://"+str(self.url)
        return url