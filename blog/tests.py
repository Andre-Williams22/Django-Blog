from django.test import TestCase, Client
from django.urls import resolve 
from django.http import HttpRequest
from blog.views import about

from django.contrib.auth.models import User
from blog.models import Post

class AboutTest(TestCase):
    def test_about_page_returns_correct_html(self):

        response = self.client.get('/about/')
        
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '<h1>About Page</h1>')



class BlogTest(TestCase):
    def test_about_page_returns_correct_html(self):

        response = self.client.get('/blog/')
        
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '<h1>Welcome</h1>')




class BlogTestCase(TestCase):
    def test_true_is_true(self):
        """ Tests if True is equal to True. Should always pass. """
        self.assertEqual(True, True)





# # def test_multiple_posts(self):
# #     # dummy data 
# #     user = User()
# #     user.save()

# #     Post.objects.create()

# #     post_1 = Post(title='Blog 1', content='First Post Content', author=user)
#     # post_1.save()
#     # post_2 = Post(title='Blog 2', content='Sky is beautiful', author=user)
#     # post_2.save()


#     # self.assertEqual(post_1.slug, "Blog 1")


# class PostListViewTests(TestCase):

#     def test_many_posts(self):

        # user = User()
        # user.save()

        # post_1 = Post(title='Blog 1', content='First Post Content', author=user)
        # post_2 = Post(title='Blog 2', content='Sky is beautiful', author=user)
        # post_1.save()
        # post_2.save()


        # # make a get request 
        # response = self.client.get('/')

        # # check status
        # self.assertEqual(response.status_code, 200)

        # posts = response.context['posts']

        # #self.assertEqual(len(posts), 2)
        # self.assertContains(response, 'Blog 1')
        # self.assertContains(response,'Sky is beautiful')
        # self.assertQuerysetEqual(
        #     posts,
        #     ['<Page: Blog 1>', '<Blog 2>'],
        #     ordered=False
        # )



