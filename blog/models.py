from django.db import models

# Create your models here.

class Category(models.Model):
    cate_name = models.CharField("이름", max_length=50)
    description = models.TextField("설명")

    def __str__(self):
        return self.cate_name


class Article(models.Model):
    def __str__(self):
        return self.title
    title = models.CharField("타이틀", max_length=100)
    user = models.ForeignKey('user.User', verbose_name="작성자", on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category, verbose_name="카테고리")
    content = models.TextField("내용")

