from django.urls import path
from . import views

urlpatterns = [
    path("", views.ReviewView.as_view()),
    path("thank-you", views.ThankYouView.as_view()),
    path("reviews", views.ReviewsListView.as_view()),
    path("reviews/favorite", views.AddFavoriteView.as_view()),   # we put the reviews/favorite first because we do not wand the favorite to be treaded as a primary key.
    path("reviews/<int:pk>", views.SingleReviewView.as_view())
]