from django.db import models
from django.utils import timezone 
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


    def get_absolute_url(self):
        return reverse("post-detail", kwargs={"pk": self.pk})
    


# python manage.py makemigrations 
# python manage.py migrate 
# python manage.py shell 
# from blog.models import Post
# 

# User.objects.all()
# User.objects.first()
# User.objects.filter(username='andre')
# User.objects.filter(username='andre').first 

# user = User.objects.filter(username='andre')
# or 
# user = User.objects.get(id=1)
# user

# post_1 = Post(title='Blog 1', content='First Post Content', author=user)
# post_1.save()

# post_2 = Post(title='Blog 2', content='Sky is beautiful', author_id=user.id)
# post_2.save()

# post = Post.objects.first()
# post.content 
# post.date_posted
# post.author.email
# user.post_set.all() ## shows all their post

# Pagination
# 
# import json                                                                                                                                          
#from blog.models import Post   
#  
# with open('posts.json') as f: 
#    posts_json = json.load(f) 
#                                                                                                                                                                                                                                                                                                                  

# for post in posts_json: 
#    post = Post(title=post['title'], content=post['content'], author_id=post['user_id']) 
#    post.save() 


# from django.core.paginator import Paginator  
# posts = []
# posts = ['1', '2', '3', '4', '5']  
# p = Paginator(posts, 2)
# p.num_pages
# for page in p.page_range:
#   print(page)
# p1 = p.page(1)
# p1.number 
# p1.object_list
# p1.has_next()
# p1.next_page_number() 