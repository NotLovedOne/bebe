from django import template
from movies.models import Category, Movie


register = template.Library()


@register.simple_tag()
def getcategories():
    """Вывод всех категорий"""
    return Category.objects.all()


@register.inclusion_tag('movies/tags/last_movie.html')
def getlastmovies(count=5):
    movies = Movie.objects.order_by("-id")[:count]