from django.db import models

class Diak(models.Model):
    azonosito = models.IntegerField(max_length = 11)
    nev = models.CharField(max_length = 256)
    szak = models.CharField(max_length = 256)
    pont = models.IntegerField(max_length=3)
    megfelelt = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Diák'
        verbose_name_plural = 'Diákok'

    def __str__(self):
        """Unicode representation of Kerdes."""
        return f"A szóban forgó diák neve {self.nev}"