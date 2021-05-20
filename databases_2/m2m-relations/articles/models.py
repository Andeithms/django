from django.db import models


class Article(models.Model):

    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение',)

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def __str__(self):
        return self.title


class Tag(models.Model):
    title = models.CharField(max_length=32, verbose_name='Тег')
    articles = models.ManyToManyField(Article, related_name='tags', through='Relationship')

    class Meta:
        verbose_name = 'Темa'
        verbose_name_plural = 'Темы'

    def __str__(self):
        return self.title


class Relationship(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    main = models.BooleanField(verbose_name='Основная')

    def __str__(self):
        return '{0} {1}'.format(self.article, self.tag)