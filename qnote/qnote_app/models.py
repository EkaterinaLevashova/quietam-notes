from django.db import models


# If don't create the PrimaryKey - Django will create ID
class User(models.Model):
    name = models.CharField(max_length=256)
    email = models.EmailField(max_length=256)

    def __str__(self):
        return self.name


class Note(models.Model):
    author = models.ForeignKey(User,
                               related_name='notes',
                               on_delete=models.CASCADE)
    title = models.CharField(max_length=256)
    note = models.CharField(max_length=256)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
