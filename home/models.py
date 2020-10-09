from django.db import models
from django.urls import reverse

from news.settings import AUTH_USER_MODEL


class Categpry(models.Model):
    name = models.CharField(max_length=50)
    img = models.ImageField(upload_to='static/img/category-img/')
    

    class Meta:
        verbose_name = "Categpry"
        verbose_name_plural = "Categprys"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Categpry_detail", kwargs={"pk": self.pk})


class Blog(models.Model):
    title = models.CharField(max_length=50)
    date_add = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='static/img/blog/%Y/%m/%d/', height_field=None, width_field=None, max_length=None)
    reporter = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField()
    categorie = models.ForeignKey(Categpry, on_delete=models.CASCADE)
    status = models.BooleanField(default=True)
    viewer = models.IntegerField(default=0)
    

    class Meta:
        verbose_name = "Blog"
        verbose_name_plural = "Blogs"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("Blog_detail", kwargs={"pk": self.pk})
    
    def deactive(self):
        self.status = False
        self.save()