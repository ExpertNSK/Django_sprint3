from django.db import models


class AbstractModel(models.Model):
    '''Abstract model.'''
    is_published = models.BooleanField(
        default=True
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        abstract = True
