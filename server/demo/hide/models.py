from django.db import models

# 'index', 'file_path', 'state', 'priority'
class HideList(models.Model):
    index = models.IntegerField(db_column="INDEX", primary_key=True)
    file_path = models.CharField(db_column="FILE_PATH", max_length=200)
    state = models.BooleanField(db_column="STATE")
    priority = models.IntegerField(db_column="PRIORITY")