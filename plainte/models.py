from django.db import models
from django.contrib.auth.models import User

class Report(models.Model):
    Categorie = [
        ('dechets', 'Déchets'),
        ('route', 'Route endommagée'),
        ('coupure', "Coupure d'eau ou de courant"),
        ('eclairage', 'Éclairage public'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE) 
    category = models.CharField(max_length=50)
    description = models.TextField()
    location = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.category} signalé par {self.user.username}"