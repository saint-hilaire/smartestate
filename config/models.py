from django.db import models

# Create your models here.

#################
# Configuration #
#################

class Config(models.Model):

    # See https://stackoverflow.com/questions/39412968/allow-only-one-instance-of-a-model-in-django
    def save(self, *args, **kwargs):
        self.pk = self.id = 1
        return super().save(*args, **kwargs)

    site_title = models.CharField(max_length=32, default='SmartEstate',
        null=True, blank=True)

    cover_text = models.TextField(max_length=4096,
        default='Welcome to SmartEstate! SmartEstate lets real estate owners, brokers, managers, landlords, etc. manage their listings all from one conventient, cloud native web app. Please stay tuned, more info is coming soon.',
        null=True, blank=True,
        help_text='The text displayed on the front page of your site')

    THEMES = (
        ('base','BASE'),
        ('frankfurt','FRANKFURT'),
        ('wiesbaden','WIESBADEN'),
        ('munich','MUNICH'),
    )
    theme = models.CharField(max_length=16, default='base', choices=THEMES)

    # See Feature #326: When we have a logo for our app, set it as default here.
    # Users can replace it with their own, or remove altogether.
    logo_image = models.ImageField(upload_to='uploads/config/',
        blank=True, null=True)

    show_filter_search_on_homepage = models.BooleanField(default=True)
    show_filter_search_in_listview = models.BooleanField(default=True)

    def __str__(self):
        return "Site configuration"
