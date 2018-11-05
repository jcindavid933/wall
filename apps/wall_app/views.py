from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *

def index(request):
    if "login_id" not in request.session:
        return redirect ('/')
    message = Message.objects.all()
    comment = Comment.objects.all()
    context = {
        'messages': message,
        'comments': comment
    }
    return render(request, 'wall_app/index.html', context)

def message(request):
    if request.method == 'POST':
        message = Message.objects.create(message=request.POST['message'], user=User.objects.get(id=request.session['login_id']))
    return redirect('/wall')

def delete_message(request):
    x = Message.objects.filter(user=User.objects.get(id=request.session['login_id']))
    x.delete()
    request.session['message'] = ''
    return redirect('/wall')

def comment(request):
    if request.method == 'POST':
        a = request.POST['comment']
        b = User.objects.get(id=int(request.session['login_id']))
        c = Message.objects.get(id=request.POST['comment_id'])
        comment = Comment.objects.create(comment=a, user_msg=b, comment_msg=c)
    return redirect('/wall')
