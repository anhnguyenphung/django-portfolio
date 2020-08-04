# A Simple Blog Page Built From Django Framework
![project-page-photo](https://github.com/anhnguyenphung/django-portfolio/blob/master/images/project_page.png)
---

## Introduction
After learning Django, a Python-based web framework, I decided to practice what I have learned by creating a simple blog page. In this blog page, you can view projects and posts
as well as comment on the posts. Moreover, with the Django shell and admin, you can also add, modify, or delete projects and posts.

## Basic Usage
You can use this project by cloning the repository with Git command:
```
git clone https://github.com/anhnguyenphung/django-portfolio
```
Then move to the directory that you just have downloaded by opening the Command Prompt or the Bash shell:
```shell
cd django-portfolio
```
To activate the blog page server, run the following command:
```shell
python manage.py runserver
```
Now you can access the blog page by visiting http://localhost:8000/django_project/ in your web browser. The home page displays all of the projects. The blog page of the site
should display something like this:
![blog-page-photo](https://github.com/anhnguyenphung/django-portfolio/blob/master/images/blog_page.png)

## Make Changes to Projects in Blog Page
To make changes to projects in the page, you access the Django shell with the following command:
```shell
python manage.py shell
```
Then you import the the project model:
```python
from django_project.models import Django_Project
```
To access all of existing projects:
```python
Django_Project.objects.all()
```
To add a project, you can create an instance of Django_Project:
```python
p = Django_Project(title='My Project', description='A web development project.', technology='Django', image='img/project.png')
```
```python
p.save()
```
Remember to add the image **"project.png"** of your choice in the folder **/django_project/static/img/**

To modify an existing project, you can access that project by its key and modify its attributes. For example:
```python
p = Django_Project.objects.get(pk = 1)
```
```python
p.title = 'My New Project'
```
To delete an existing project, you can access that object by its key and delete that project. For example:
```python
p = Django_Project.objects.get(pk = 1)
```
```python
p.delete()
```

## Make Changes to Posts in Blog Page
To make changes to posts in blog page, you access the Django admin page by visiting http://localhost:8000/admin/. Remember to activate the blog page server first. Then you can
log in to Django admin with the username **user** and the password **admindjango** that I set by default. Later on, you can custom your own username and password in the Django
admin site.

When you first log in to the Django admin site, in the Home page, you can view and edit user information (username and password) by clicking **Users** in 
**AUTHENTICATION AND AUTHORIZATION**. To add, modify, or delete posts, you can clicking **Posts** in **DJANGO_BLOG**. When editing your post, you can even add the category
to distinguish your posts.

![admin-page-photo](https://github.com/anhnguyenphung/django-portfolio/blob/master/images/admin_page.png)

Remember that when you delete a post, all of the comments associated with that post will be dissapeared.

## Conclusion
Thanks to this [Django tutorial](https://realpython.com/get-started-with-django-1/), I could successfully finish this blog page. With this project, I have learned how to build
a website with Django framework:
* Add web pages with views and templates.
* Get user input with forms.
* Hook views and templates up with URL configurations.
* Add data to my site using relational databases with Django’s Object Relational Mapper.
* Use the Django Admin to manage your models.
