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
    title = models.CharField(max_length=128, unique=True)
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

    def save(self, *args, **kwargs):
        super(Session, self).save(*args, **kwargs)

# Class to store players
class Player(models.Model):
    session = models.ManyToManyField(Session)
    gender = models.CharField(max_length=1)
    age = models.IntegerField()
    nationality = models.CharField(max_length=128)

    def save(self, *args, **kwargs):
        super(Player, self).save(*args, **kwargs)

# Class to store answers
class Answer(models.Model):
    session = models.ManyToManyField(Session)
    statement = models.ManyToManyField(Statement)
    player = models.ManyToManyField(Player)
    answer = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        super(Answer, self).save(*args, **kwargs)