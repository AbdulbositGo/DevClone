from django.db import models

# Create your models here.


class Tag(models.Model):
    COLORS = [
        ('DF', 'blue'),
        ('DK', 'gray'),
        ('RD', 'red'),
        ('GR', 'green'),
        ('YL', 'yellow'),
        ('ID', 'indigo'),
        ('PP', 'purple'),
        ('PK', 'pink'),
    ]
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=256, null=True, blank=True)
    color = models.CharField(max_length=2, choices=COLORS, default='DF')

    def __str__(self):
        return f"# {self.name}"
