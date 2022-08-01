from django.db import models


class createDevocional(models.Model):
    theme = models.CharField(max_length=35, default='Tema')
    image = models.ImageField(default='default.jpg', upload_to='%m')
    verse = models.TextField(default='Jesus chorou.')
    reference = models.CharField(max_length=50, default='João 11:35')
    text = models.TextField(default='Jesus nos ama')
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.id}"


class newsLetter(models.Model):
    email = models.EmailField()
    username = models.CharField(default="Usuário", max_length=200)


all_classes = [
    createDevocional,
    newsLetter,
]