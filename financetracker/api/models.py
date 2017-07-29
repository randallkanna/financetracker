from django.db import models

class List(models.Model):
    name = models.CharField(max_length=255, blank=False, unique=True)
    owner = models.ForeignKey('auth.User',
                              related_name='lists',
                              on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{}".format(self.name)