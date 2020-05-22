from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.forms.models import *

# 'index', 'file_path', 'state'
class Myfile(models.Model):
    class Meta:
        unique_together = (('author', 'index'))
    index = models.IntegerField(db_column="INDEX")
    file_path = models.CharField(db_column="FILE_PATH", max_length=200)
    state = models.BooleanField(db_column="STATE")
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    # def __str__(self):
    #     return "index=" + str(self.index) + ", file_path=" + self.file_path

    #
    # def validate_unique(self, *args, **kwargs):
    #     super(Myfile, self).validate_unique(*args, **kwargs)
    #     """
    #     Call the instance's validate_unique() method and update the form's
    #     validation errors if any were raised.
    #     """
    #     exclude = self._get_validation_exclusions()
    #     try:
    #         self.instance.validate_unique(exclude=exclude)
    #         return True
    #     except ValidationError as e:
    #         return False

