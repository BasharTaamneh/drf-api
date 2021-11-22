from django.db import models
from django.contrib.auth import get_user_model


class Electro(models.Model):
    elctronic_name = models.CharField(max_length=64)
    elctronic_image = models.ImageField(upload_to='Electro/thumbnail/%Y/%m/%d/', null=True, blank=True)
    description = models.TextField()
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.elctronic_name
