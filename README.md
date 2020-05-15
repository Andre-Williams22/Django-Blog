# Django-Blog


![Blog Site](https://github.com/Andre-Williams22/Django-Blog/blob/master/media/screenshot.jpg)

## About 
This blog is a platform for machine learning and data enthusiasts to share valuable content to the world. User's can contribute to the blog and add their own personalization with different types of content and robust profile pictures to make their prescence known.


## Author

[Andre Williams](https://www.linkedin.com/in/andrewilliams22/) 

## Live Deployment 

https://machinelearningblog.herokuapp.com/

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites
If you haven't already installed pip3 for Python3
```
sudo apt install python3-pip
```
Install Django 
```
pip3 install django
pip3 install PILLOW
pip3 install boto3 
pip3 install django-storages
pip3 install gunicorn
pip3 install psycopg2==2.7.5
pip3 django-heroku
```

### Installing

1. Clone the respository
```
git clone (repo link)
```
2. Make sure in the correct directory
```
cd django-blog
```
3. python3 manage.py runserver 

You should see something similar to the output below:
```
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
May 15, 2020 - 16:05:35
Django version 3.0.6, using settings 'blog_site.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```
## Running the tests
```
python3 manage.py test
```

## Built With

* Django 
* Amazon s3 
* Heroku 

