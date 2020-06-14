from django.db import models
from django.contrib.auth.models import User

class Myfile(models.Model):
    class Meta:
        unique_together = (('author', 'file_path'))
    file_path = models.CharField(db_column="FILE_PATH", max_length=200)
    state = models.BooleanField(db_column="STATE")
    author = models.ForeignKey(User, on_delete=models.CASCADE)


class NetworkState(models.Model):
    network_state = models.BooleanField(db_column="NETWORK_STATE", default="False")
    author = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
