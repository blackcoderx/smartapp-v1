from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


# events
class Event(models.Model):
    host = models.ForeignKey(User, on_delete=models.CASCADE, related_name='events')
    name = models.CharField(max_length=500)
    # location = models.ForeignKey(Location, on_delete=models.SET_NULL,)
    date = models.DateField()
    attendees = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f'{self.host.first_name} {self.host.last_name}'


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    content = models.TextField()
    image = models.ImageField(upload_to='posts/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name_plural = 'posts'

    def __str__(self):
        return f'Post by {self.author.first_name} {self.author.last_name}'

# medicals
