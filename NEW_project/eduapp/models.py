from django.db import models
from helpapp.models import TimeStamp, generate_unique_slug


class Science(TimeStamp):
    name = models.CharField(max_length=50)
    author = models.CharField(max_length=50, null=True, blank=True)
    image = models.ImageField(upload_to='sciences', null=True, blank=True)
    slug = models.SlugField(null=True, blank=True, unique=True, max_length=255)

    class Meta:
        indexes = [
            models.Index(fields=['slug']),
        ]
        ordering = ['id']

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            if len(self.name) > 0:
                self.slug = generate_unique_slug(self)

        super(Science, self).save(*args, **kwargs)


class Question(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='questions', null=True, blank=True)
    slug = models.SlugField(null=True, blank=True, unique=True, max_length=255)
    science = models.ForeignKey(Science, related_name='question', on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        indexes = [
            models.Index(fields=['slug']),
        ]
        ordering = ['id']

    def __str__(self):
        return (self.name)

    def save(self, *args, **kwargs):
        if not self.slug:
            if len(self.name) > 0:
                self.slug = generate_unique_slug(self)

        super(Question, self).save(*args, **kwargs)
