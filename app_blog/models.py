from django.db import models

class createDevocional(models.Model):
    theme = models.CharField(max_length=30, default='Tema')
    # image = models.ImageField()
    verse = models.TextField(default='Jesus chorou.')
    reference = models.CharField(max_length=50, default='João 11:35')
    text = models.TextField(default='Jesus nos ama')

    def __str__(self):
        return f"{self.id}"


all_classes = [
    createDevocional
]