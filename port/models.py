from django.db import models
from PIL import Image
from django.core.files.storage import default_storage as storage


class Project(models.Model):
    image = models.ImageField(upload_to='images/', null=False, blank=False)
    title = models.CharField(max_length=200)
    tool1 = models.CharField(max_length=255)
    tool2 = models.CharField(max_length=255)
    tool3 = models.CharField(max_length=255)
    link1 = models.URLField(max_length=500)
    link2 = models.URLField(max_length=500)
    list_date = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Project"

    def save(self, *args, **kwargs):
        if not self.title:
            return

        super(Project, self).save()
        if self.image:
            size = 300, 300
            image = Image.open(self.image)
            image.thumbnail(size, Image.ANTIALIAS)
            fh = storage.open(self.image.name, "w")
            format = "png"
            image.save(fh, format)
            fh.close()


class About(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='images/', null=False, blank=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "About"

    def save(self, *args, **kwargs):
        if not self.title and self.description:
            return

        super(About, self).save()
        if self.image:
            size = 300, 300
            image = Image.open(self.image)
            image.thumbnail(size, Image.ANTIALIAS)
            fh = storage.open(self.image.name, "w")
            format = "png"
            image.save(fh, format)
            fh.close()


class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    message = models.TextField()

    def __str__(self):
        return f'{self.name} - {self.email}'

    class Meta:
        verbose_name_plural = "Contact"

