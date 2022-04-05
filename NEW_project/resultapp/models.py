from django.db import models
from userapp.models import User
from eduapp.models import Science
from helpapp.models import TimeStamp

class Result(TimeStamp):
    userball = models.PositiveIntegerField()
    maxball = models.PositiveIntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='result', null=True, blank=True)
    science = models.ForeignKey(Science, on_delete=models.CASCADE, related_name='result', null=True, blank=True)


    def __str__(self):
        return self.user.phone + ': ' + str(self.userball) + '/' + str(self.maxball)

