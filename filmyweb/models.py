from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL




# Create your models here.
class Film(models.Model):
    author = models.ForeignKey(User,default=1,null=True,on_delete=models.SET_NULL,)
    tytul = models.CharField(max_length=64, blank=False, unique=True)
    rok = models.PositiveSmallIntegerField(default=2000)
    krotki_opis = models.TextField(default="", max_length=195, blank=False, null=True)
    opis = models.TextField(default="")
    premiera = models.DateField(null=True, blank=True)
    imbd_rating = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    plakat = models.ImageField(upload_to="plakaty", null=True, blank=True)
    likes = models.ManyToManyField(User, related_name='poj_likes')

    def total_likes(self):
        return  self.likes.count()


    def __str__(self):
        return self.film_i_rok()

    def film_i_rok(self):
        return "{} ({})".format(self.tytul, self.rok)

class Comments(models.Model):
    post = models.ForeignKey(Film, null=True, on_delete=models.CASCADE, related_name='comments')
    komentarz = models.TextField(default="", max_length=1000)
    date_added = models.DateField(auto_now_add=True)
    aut = models.ForeignKey(User, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.komentarz;