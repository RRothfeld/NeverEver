from django.db import models
from django.template.defaultfilters import slugify

# Class to store categories
class Category(models.Model):
    name = models.CharField(max_length=128, unique=True)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.name

# Class to store statements
class Statement(models.Model):
    categories = models.ManyToManyField(Category)
    sessions = models.ManyToManyField(Session)
    title = models.CharField(max_length=128)
    views = models.IntegerField(default=0)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Statement, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.title

# Class to store play sessions
class Session(models.Model):
    statements = models.ManyToManyField(Statement)
    id = models.CharField(max_length=128)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Session, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.id

# Class to store players
class Player(models.Model):
    session = models.ManyToOneField(Session)
    id = models.IntegerField(default=0)
    gender = models.CharField(max_length=1)
    age = models.IntegerField()
    nationality = models.CharField(max_length=128)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Session, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.id

# Class to store answers
class Anwser(models.Model):
    session = models.ManyToOneField(Session)
    statement = models.ManyToOneField(Statement)
    id = models.IntegerField(default=0)
    answer = models.BooleanField()
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Anwser, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.id