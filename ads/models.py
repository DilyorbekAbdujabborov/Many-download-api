from django.db import models

class Media(models.Model):
    title = models.CharField(max_length=255)
    url = models.URLField()
    video_file = models.FileField(upload_to='videos/')
    created_at = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)
    start_at = models.DateTimeField(null=True, blank=True)
    end_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.title

    def is_active(self):
        from django.utils import timezone
        now = timezone.now()
        return self.active and (self.start_at <= now <= self.end_at)
