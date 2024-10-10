from django.db import models

class Subscription(models.Model):
    # Define your model fields here
    name = models.CharField(max_length=255)

    class Meta:
        permissions = [
            ("basic", "Basic Perm"),
            ("basic_ai", "Basic AI Perm"),
            ("pro", "Pro Perm"),
            ("advanced", "Advanced Perm"),
        ]

    def __str__(self):
        return self.name