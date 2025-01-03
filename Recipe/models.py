from django.db import models
from django.conf import settings
from django.utils import timezone

# Managers
class PublishManager(models.Manager):
    def get_queryset(self):
        return (
            super().get_queryset().filter(status=Recipe.Status.PUBLISHED)
        )

class FlagManager(models.Manager):
    def get_queryset(self):
        return(
            super().get_queryset().filter(status=Recipe.Status.FLAGGED)
        )

class AdminFlagManager(models.Manager):
    def get_queryset(self):
        return(
            super().get_queryset().filter(status=Recipe.Status.ADMIN_FLAGGED)
        )


class Recipe(models.Model):
    class Status(models.TextChoices):
        DRAFT = 'DF','Draft'
        PUBLISHED = 'PUB','Published'
        FLAGGED = 'FG','Flagged'
        ADMIN_FLAGGED = 'AFG','AdminFlagged'

    title = models.CharField(max_length=255)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='recipes')
    slug = models.SlugField(max_length=255)
    ingredient = models.TextField()
    directions = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=25, choices=Status, default=Status.DRAFT)
    objects = models.Manager()
    published = PublishManager()
    flagged = FlagManager()
    adminFlagged = AdminFlagManager()


    class Meta:
        ordering = ['-publish', 'title']
        indexes = [
            models.Index(fields=['-publish', 'title']),
        ]

    def __str__(self):
        return self.title