from django.db import models


class Home(models.Model):
    title = models.CharField(max_length=255)
    sub_title = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = 'Home'
        verbose_name_plural = 'Homes'




class Services(models.Model):
    title = models.CharField(max_length=255)
    sub_title = models.CharField(max_length=255)
    icon_title = models.CharField(max_length=255)
    icon_subtitle = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = 'Service'
        verbose_name_plural = 'Services'

class Why_Us(models.Model):
    title = models.CharField(max_length=255)
    sub_title = models.CharField(max_length=255)
    text = models.TextField(max_length=255)

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = 'Why_Us'
        verbose_name_plural = 'Why_Us'


class Team(models.Model):
    title = models.CharField(max_length=255)
    name = models.CharField(max_length=30)
    job = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = 'Team'
        verbose_name_plural = 'Teams'