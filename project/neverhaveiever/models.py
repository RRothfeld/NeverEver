from django.db import models
from django.template.defaultfilters import slugify


class Category(models.Model):
    # statements = models.ManyToManyField(Statement)
    name = models.CharField(max_length=128, unique=True)
    adult_themed = models.BooleanField(default=False)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.name


class Statement(models.Model):
    categories = models.ManyToManyField(Category)
    title = models.CharField(max_length=128)
    views = models.IntegerField(default=0)
    no_answers = models.IntegerField(default=0)
    yes_answers = models.IntegerField(default=0)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Statement, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.title