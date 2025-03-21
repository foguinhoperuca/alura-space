from datetime import datetime
from typing import List, Tuple

from django.contrib.auth.models import User
from django.db import models


CATEGORY_OPTIONS: List[Tuple[str, str]] = [
    ("NEBULA", "nebula"),
    ("STAR", "star"),
    ("galaxy", "galaxy"),
    ("PLANET", "planet"),
]


class Photograph(models.Model):
    name = models.CharField(max_length=128, null=False, blank=False)
    legend = models.CharField(max_length=512, null=False, blank=False)
    description = models.TextField(null=False, blank=False)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    category = models.CharField(max_length=128, null=False, blank=False, choices=CATEGORY_OPTIONS, default="")
    published = models.BooleanField(default=False)
    photo_date = models.DateTimeField(default=datetime.now, blank=False)
    user = models.ForeignKey(to=User, on_delete=models.SET_NULL, null=True, blank=False, related_name='user')

    def __str__(self):
        return f"Photograph: [name={self.name}]"
