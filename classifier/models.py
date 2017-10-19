from django.db import models


class Verb(models.Model):
    BCL_CHOICES = (
        ('Creating', 'Creating'),
        ('Evaluating', 'Evaluating'),
        ('Analyzing', 'Analyzing'),
        ('Applying', 'Applying'),
        ('Understanding', 'Understanding'),
        ('Remembering', 'Remembering'),
    )
    verb = models.CharField(max_length=30)
    category = models.CharField(max_length=20, choices=BCL_CHOICES)

    def __str__(self):
        return '%s -------------> %s' % (self.verb, self.category)
