from django.db import models

class About(models.Model):
    title = models.CharField(max_length=255)
    sub_title = models.CharField(max_length=255)
    text_title = models.CharField(max_length=255)
    text_sub_title = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = 'About'
        verbose_name_plural = 'Abouts'