from django.core.cache import cache
from django.test import Client, TestCase
from django.urls import reverse


class MoviesTest(TestCase):
    def setUp(self):
        self.client = Client()
        cache.clear()

    def test_view_movies_correct_template(self):
        """check if the right template is called"""
        response = self.client.get(reverse('cinema:films'))
        self.assertTemplateUsed(response, 'cinema/movies.html')

    def test_view_movies(self):
        """Verify that all movies are retrieved"""
        response = self.client.get(reverse('cinema:films'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '</table>')
        self.assertContains(response, '<title>Movies</title>')

    def test_fetch_movies_pagination_is_10(self):
        """Verify that movies are returned based on the paginated default value per page"""
        response = self.client.get(reverse('cinema:films'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['movies']), 10)

    def test_fetch_single_movie(self):
        """Verify that a single movie is retrieved"""
        movie_response = self.client.get(reverse('cinema:films'))
        movie_id = list(movie_response.context['movies'])[0]['id']
        response = self.client.get(reverse('cinema:film', args=(movie_id,)))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'cinema/movie.html')
        self.assertContains(response, 'Cast')
