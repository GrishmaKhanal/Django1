from django.db import models

# it should show to templates
class Introduction(models.Model ):
    name = models.CharField(max_length=40)
    roll_no = models.IntegerField()
    college = models.CharField(max_length=40)
    faculty = models.CharField(max_length=5)
    def __str__(self):
        return f"{self.name} - {self.roll_no}"