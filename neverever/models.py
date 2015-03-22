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
    likes = models.IntegerField(default=0)
    slug = models.SlugField(unique=True)
    nsfw = models.BooleanField(default=True)
    likes = models.IntegerField(default=0)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Statement, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.title


# Class to store play sessions
class Session(models.Model):
    # stamp = models.IntegerField(null=True) # TODO: change to stamp = models.IntegerField(primary_key=True)
    sid = models.CharField(max_length=128, null=True)  # TODO: change to stamp = models.IntegerField(primary_key=True)
    categories = models.ManyToManyField(Category)
    nsfw = models.BooleanField(default=False)
    num_players = models.IntegerField(default=1)
    last_modified = models.DateTimeField(auto_now_add=True, blank=True)

    # Testing
    last_statement = models.ForeignKey(Statement, null=True, related_name="last_statement")
    used_statements = models.ManyToManyField(Statement, null=True, related_name="used_statements")

    # Tried myself on ITERABLES, did not work
    # def __iter__(self):
    #    return iter("session" + str(self.id))

    def __unicode__(self):
        return "Session " + str(self.sid)


# Class to store players
class Player(models.Model):
    stamp = models.IntegerField(primary_key=False)  # TODO: CHANGE TO True
    session = models.ForeignKey(Session)
    # id = models.IntegerField(primary_key=True)
    gender = models.CharField(max_length=1, null=True)
    age = models.IntegerField(null=True)
    nationality = models.CharField(max_length=128, null=True)
    name = models.CharField(max_length=128, null=True)
    # slug = models.SlugField(unique=True)

    # def save(self, *args, **kwargs):
    #     self.slug = slugify(self.id)
    #     super(Player, self).save(*args, **kwargs)

    def __unicode__(self):
        return "Player " + str(self.stamp)


# Class to store answers
class Answer(models.Model):
    stamp = models.IntegerField(primary_key=True)
    session = models.ForeignKey(Session, null=True)
    statement = models.ForeignKey(Statement, null=True)
    player = models.ForeignKey(Player, null=True)
    answer = models.BooleanField(default=False)
    # id = models.IntegerField(primary_key=True)
    # slug = models.SlugField(unique=True)

    # def save(self, *args, **kwargs):
    #    self.slug = slugify(self.id)
    #    super(Answer, self).save(*args, **kwargs)

    def __unicode__(self):
        return "Answer " + str(self.stamp)


class Result(models.Model):
    statement = models.ForeignKey(Statement)
    gender = models.CharField(max_length=128, null=True)
    age = models.IntegerField(null=True)
    nationality = models.CharField(max_length=128, null=True)
    answer = models.BooleanField(default=False)

    def __unicode__(self):
        return "result_" + str(self.id)


class GlobalCounter(models.Model):
    total_sessions = models.IntegerField()
    total_players = models.IntegerField()

    def __unicode__(self):
        return "GlobalCounter " + str(self.id)
