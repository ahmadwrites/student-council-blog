from django.shortcuts import render, redirect
from .models import Post, Announcement, About
from .forms import EmailForm, CommentForm
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings


def home(request):
    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            form.save()
            save_it = form.save(commit=False)
            save_it.save()

            message = 'Hello!\nThank you for subscribing to Ahmad\'s blog!'
            subject = 'Subscription Confirmed!'
            from_email = settings.EMAIL_HOST_USER
            to_list = [save_it.email]

            send_mail(subject, message, from_email, to_list, fail_silently=True)

            messages.success(request, f'You have signed up for the newsletter!')
            return redirect('blog-home')

    else:
        form = EmailForm()

    context = {
        'posts': Post.objects.all().order_by('-date_posted')[0:4],
        'form': form,
        'title': 'Home',
        'announcements': Announcement.objects.all().order_by('-date_posted')[0:3]
    }

    return render(request, 'blog/home.html', context)


def writings(request):
    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            form.save()
            save_it = form.save(commit=False)
            save_it.save()

            message = 'Hello!\nThank you for subscribing to Ahmad\'s blog!'
            subject = 'Subscription Confirmed!'
            from_email = settings.EMAIL_HOST_USER
            to_list = [save_it.email]

            send_mail(subject, message, from_email, to_list, fail_silently=True)

            messages.success(request, f'You have signed up for the newsletter!')
            return redirect('blog-home')

    else:
        form = EmailForm()

    context = {
        'posts': Post.objects.all().order_by('-date_posted'),
        'most_viewed_articles': Post.objects.all().order_by('-views')[0:3],
        'form': form,
        'title': 'Writings'
    }
    return render(request, 'blog/writings.html', context)


def about(request):
    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            form.save()
            save_it = form.save(commit=False)
            save_it.save()

            message = 'Hello!\nThank you for subscribing to Ahmad\'s blog!'
            subject = 'Subscription Confirmed!'
            from_email = settings.EMAIL_HOST_USER
            to_list = [save_it.email]

            send_mail(subject, message, from_email, to_list, fail_silently=True)

            messages.success(request, f'You have signed up for the newsletter!')
            return redirect('blog-home')

    else:
        form = EmailForm()

    context = {
        'form': form,
        'title': 'About',
        'about': About.objects.all().first()
    }
    return render(request, 'blog/about.html', context)


def contact(request):
    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            form.save()
            save_it = form.save(commit=False)
            save_it.save()

            message = 'Hello!\nThank you for subscribing to Ahmad\'s blog!'
            subject = 'Subscription Confirmed!'
            from_email = settings.EMAIL_HOST_USER
            to_list = [save_it.email]

            send_mail(subject, message, from_email, to_list, fail_silently=True)

            messages.success(request, f'You have signed up for the newsletter!')
            return redirect('blog-home')

    else:
        form = EmailForm()

    context = {
        'form': form,
        'title': 'Contact'
    }
    return render(request, 'blog/contact.html', context)


def details(request, slug):
    current_post = Post.objects.get(slug=slug)

    # COMMENTS FORM
    if request.method == 'POST' and 'comment' in request.POST:
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)  # Take in the form and play with the model working with
            comment.post = current_post  # comment (model).post
            comment.author = request.user
            comment.save()
            messages.success(request, 'Your comment has been added')
            return redirect('blog-detail', slug)
    else:
        form = CommentForm()

    comments = current_post.comments.order_by('created')

    # EMAIL NEWSLETTER FORM
    if request.method == 'POST':
        e_form = EmailForm(request.POST)
        if e_form.is_valid():
            e_form.save()
            save_it = e_form.save(commit=False)
            save_it.save()

            message = 'Hello!\nThank you for subscribing to Ahmad\'s blog!'
            subject = 'Subscription Confirmed!'
            from_email = settings.EMAIL_HOST_USER
            to_list = [save_it.email]

            send_mail(subject, message, from_email, to_list, fail_silently=True)

            messages.success(request, f'You have signed up for the newsletter!')
            return redirect('blog-detail', slug)

    else:
        e_form = EmailForm()

    context = {
        'post': Post.objects.get(slug=slug),
        'other_articles': Post.objects.all().exclude(slug=current_post.slug).order_by('-date_posted')[0:3],
        'title': current_post.title,
        'form': form,
        'e_form': e_form,
        'comments': comments,
    }

    current_post.views += 1
    current_post.save(update_fields=['views'])

    return render(request, 'blog/post.html', context)


def topics(request, topic):
    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            form.save()
            save_it = form.save(commit=False)
            save_it.save()

            message = 'Hello!\nThank you for subscribing to Ahmad\'s blog!'
            subject = 'Subscription Confirmed!'
            from_email = settings.EMAIL_HOST_USER
            to_list = [save_it.email]

            send_mail(subject, message, from_email, to_list, fail_silently=True)

            messages.success(request, f'You have signed up for the newsletter!')
            return redirect('blog-home')

    else:
        form = EmailForm()

    post = Post.objects.all().filter(topic__startswith=topic).order_by('-date_posted')
    topic_name = Post.objects.all().filter(topic__startswith=topic)[0]
    context = {
        'posts': post,
        'topic': topic_name,
        'most_viewed_articles': Post.objects.all().order_by('-views')[0:3],
        'form': form,
        'title': topic_name.topic
    }

    return render(request, 'blog/topics.html', context)
