from django.db import models
from django.urls import reverse

from news.settings import AUTH_USER_MODEL

import datetime

today = datetime.date.today()


class Category(models.Model):
    date_add = models.DateField(auto_now_add=True)
    name = models.CharField(max_length=50)
    img = models.ImageField(upload_to='static/img/category-img/')
    new = models.BooleanField(default=True)
    trending = models.BooleanField(default=False)
    

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categorys"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Category_detail", kwargs={"pk": self.pk})

    def not_new_anymore(self):
        self.new = False
        self.save()

    def not_trending_anymore(self):
        self.trending = False
        self.save()

    def auto_not_new(self):
        if self.date_add < today:
            self.new = False
            self.save()
        else: pass

    def auto_not_trending(self):
        if self.date_add < today:
            self.trending = False
            self.save()
        else: pass


class Blog(models.Model):
    title = models.CharField(max_length=100)
    date_add = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='static/img/blog/%Y/%m/%d/', height_field=None, width_field=None, max_length=None)
    reporter = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField()
    categorie = models.ForeignKey(Category, on_delete=models.CASCADE)
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