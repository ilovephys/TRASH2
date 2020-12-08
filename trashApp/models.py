from django.db import models

category = (
    ("bisisness", "ビジネス"),
    ("life", "生活"),
    ("other", "その他")
)



# Create your models here.
class BlogModel(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    postdate = models.DateField(auto_now_add=True)
    category = models.CharField(
        max_length=50,
        choices=category
    )

    def __str__(self):
        return self.title

class BlogDetail(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    postdate = models.DateField(auto_now_add=True)
    category = models.CharField(
        max_length=50,
        choices=category
    )

    def __str__(self):
        return self.title