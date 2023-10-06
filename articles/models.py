from django.db import models

class Articles(models.Model):
    title = models.CharField(max_length= 200 , null=False)
    body = models.TextField(null=True)
    slug = models.SlugField()
    date = models.DateTimeField(null=False, blank=False, auto_now_add=True)
    thumb = models.ImageField(default='default.jpg', blank=True)
    def __str__(self):
        return self.title
    
    def snippet(self):
        if len(self.body) > 50:
            return self.body[:50] + "..."
        return self.body