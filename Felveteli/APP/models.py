from django.db import models

class Diak(models.Model):
    azonosito = models.IntegerField()
    nev = models.CharField(max_length = 256)
    szak = models.CharField(max_length = 256)
    pont = models.IntegerField()
    megfelelt = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Diák'
        verbose_name_plural = 'Diákok'

    def __str__(self):
        """Unicode representation of Kerdes."""
        return f"A szóban forgó diák neve {self.nev}"