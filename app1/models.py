from django.db import models

# Create your models here.

class AllServers(models.Model):
    servers = models.CharField(max_length=128,unique=True)
    ip = models.GenericIPAddressField()
    def __unicode__(self):
        return self.servers
