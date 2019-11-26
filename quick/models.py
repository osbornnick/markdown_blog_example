from django.db import models
import markdown


class Post(models.Model):
    title = models.CharField(max_length=255)
    md = models.FileField(null=True)
    content = models.TextField(default="", editable=False)

    def save(self, *args, **kwargs):
        file = self.md
        decoded = file.read().decode('utf-8')
        extensions = ['fenced_code', 'codehilite']
        output = markdown.markdown(decoded, extensions=extensions)
        self.content = output
        super().save(*args, **kwargs)

    # unnecessary for guide
    def __str__(self):
        return self.title
