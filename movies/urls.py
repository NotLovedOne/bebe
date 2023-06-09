from django.urls import path
from . import views

urlpatterns = [
    path ('',views.MovieView.as_view()),
    path("filter/", views.FilterMoviesView.as_view(), name='filter'),
    path("json-filter/", views.JsonFilterMoviesView.as_view(), name='json_filter'),
    path("search/", views.Search.as_view(), name='search'),
    
    path ("<slug:slug>/", views.MovieDetailView.as_view(), name = "moviesingle"),
    path("add-rating/", views.AddStarRating.as_view(), name='add_rating'),
    path("review/<int:pk>/", views.AddReview.as_view(), name="add_review"),
    path("actor/<str:slug>/", views.ActorView.as_view(), name="actor_detail"),
]