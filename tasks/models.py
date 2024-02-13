from django.db import models

# Create your models here.
from django.utils.translation import gettext_lazy as _
class Task(models.Model):
    content = models.TextField(_("content"))

    

    class Meta:
        verbose_name = _("Task")
        verbose_name_plural = _("Tasks")

    def __str__(self):
        return self.content

 