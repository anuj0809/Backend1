from django.db import models

class Music(models.Model):
    UPLOAD_MODES = (
        ("private", "private"),
        ("protected", "protected"),
        ("public", "public"),
    )
    
    title = models.CharField(max_length=100)
    uploaded_by = models.ForeignKey("users.User", on_delete=models.CASCADE)
    upload_mode = models.CharField(max_length=20,choices=UPLOAD_MODES, default="private")
    upload_date = models.DateTimeField(auto_now_add=True)
    shared_with = models.ManyToManyField("users.User", related_name="shared_with", blank=True)
    file = models.FileField(upload_to="music_files", blank=True, null=True)

    def __str__(self):
        return self.title