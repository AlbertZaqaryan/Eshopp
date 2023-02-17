from django.db import models

# Create your models here.

class HomeSliderActive(models.Model):
    title = models.CharField('HomeSliderActive title', max_length=30)
    name = models.CharField('HomeSliderActive name', max_length=50)
    about = models.TextField('HomeSliderActive about')
    img = models.ImageField('HomeSliderActive image', upload_to='media')
    logo = models.ImageField('HomeSliderActive logo', upload_to='media')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'HomeSliderActive'
        verbose_name_plural = 'HomeSlidersActive'


class HomeSlider(models.Model):
    title = models.CharField('HomeSlider title', max_length=30)
    name = models.CharField('HomeSlider name', max_length=50)
    about = models.TextField('HomeSlider about')
    img = models.ImageField('HomeSlider image', upload_to='media')
    logo = models.ImageField('HomeSlider logo', upload_to='media')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'HomeSlider'
        verbose_name_plural = 'HomeSliders'