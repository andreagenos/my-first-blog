from django.conf import settings
from django.db import models
from django.utils import timezone

class Post(models.Model): #definisce il nostro modello (è un oggetto) - Post il nome del nostro modello - models.Model è un modello Django quindi viene salvato nel datatbase
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) #questo è un link a un altro modello.
    title = models.CharField(max_length=200) #models.CharField - così si definisce un testo con un numero limitato di lettere.
    text = models.TextField() #models.TextField - questo è il codice per definire un testo senza un limite.
    created_date = models.DateTimeField(default=timezone.now) #questo per la data ed l'ora
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
# Create your models here.
