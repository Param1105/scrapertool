from django.db import models

class Proxies(models.Model):
    ipaddress = models.TextField()
    port = models.TextField()
    protocols = models.TextField()
    country = models.CharField(max_length= 5)
    uptime = models.TextField()

    def __str__(self):
        return self.ipaddress
