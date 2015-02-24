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
    # stamp = models.IntegerField(null=True) # TODO: change to stamp = models.IntegerField(primary_key=True)
    sid = models.CharField(max_length=128, null=True) # TODO: change to stamp = models.IntegerField(primary_key=True)
    categories = models.ManyToManyField(Category)
    # id = models.IntegerField(primary_key=True)
    # slug = models.SlugField(unique=True)

    # def save(self, *args, **kwargs):
    #     self.slug = slugify(self.id)
    #    super(Session, self).save(*args, **kwargs)

    # Tried myself on ITERABLES, did not work
    # def __iter__(self):
    #    return iter("session" + str(self.id))

    def __unicode__(self):
        return "Session " + str(self.sid)


# Class to store players
class Player(models.Model):
    stamp = models.IntegerField(primary_key=True)
    session = models.ManyToManyField(Session)
    # id = models.IntegerField(primary_key=True)
    gender = models.CharField(max_length=1, null=True)
    age = models.IntegerField(null=True)
    nationality = models.CharField(max_length=128, null=True)
    # slug = models.SlugField(unique=True)

    # def save(self, *args, **kwargs):
    #     self.slug = slugify(self.id)
    #     super(Player, self).save(*args, **kwargs)

    def __unicode__(self):
        return "Player " + str(self.stamp)


# Class to store answers
class Answer(models.Model):
    stamp = models.IntegerField(primary_key=True)
    session = models.ManyToManyField(Session)
    statement = models.ManyToManyField(Statement)
    player = models.ManyToManyField(Player)
    answer = models.BooleanField(default=False)
    # id = models.IntegerField(primary_key=True)
    # slug = models.SlugField(unique=True)

    # def save(self, *args, **kwargs):
    #    self.slug = slugify(self.id)
    #    super(Answer, self).save(*args, **kwargs)

    def __unicode__(self):
        return "Answer " + str(self.stamp)
