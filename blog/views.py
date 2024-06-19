from django.shortcuts import render, redirect

from authentication.models import MyUser
from .models import Post, Comment, LikePost, FollowUser
from django.contrib.auth.decorators import login_required


@login_required(login_url='/auth/login/')
def follow(request):
    follower = MyUser.objects.filter(user=request.user).first()
    following = MyUser.objects.filter(id=request.GET.get('following_id')).first()
    follow_users = FollowUser.objects.all()

    for follow_user in follow_users:
        if follow_user.follower == follower and follow_user.following == following:
            d_f = FollowUser.objects.filter(follower=follower, following=following).first()
            d_f.delete()
            return redirect('/')
    obj = FollowUser.objects.create(follower=follower, following=following)
    obj.save()

    return redirect('/')

@login_required(login_url='/auth/login/')
def like(request):
    author = MyUser.objects.filter(user=request.user).first()
    post_id = request.GET.get('post_id')
    likes = LikePost.objects.all()

    for like in likes:
        if like.author == author and str(like.post_id) == post_id:
            d_like = LikePost.objects.filter(author=author, post_id=post_id).first()
            d_like.delete()
            return redirect(f'/#{post_id}')

    obj = LikePost.objects.create(author=author, post_id=post_id)
    obj.save()


    return redirect(f'/#{post_id}')


@login_required(login_url='/auth/login/')
def create_post(request):
    if request.method == 'POST':
        author = MyUser.objects.filter(user=request.user).first()
        image = request.FILES.get('image')

    obj = Post.objects.create(author=author, image=image)
    obj.save()

    return redirect('/')


@login_required(login_url='/auth/login/')
def home_view(request):
    posts = Post.objects.filter(is_published=True)
    profile = MyUser.objects.filter(user=request.user).first()
    comments = Comment.objects.all()
    users = MyUser.objects.all()
    like = LikePost.objects.all()


    foll = [i.following for i in FollowUser.objects.filter(follower=request.user.id)]
    like_posts_author = [i.post for i in LikePost.objects.filter(author=profile)]


    for post in posts:
        post.comments = list(filter(lambda x: x.post_id == post.id, comments))
        post.likepost = len(list(filter(lambda x: x.post_id == post.id, like)))


    for user in users:
        user.followers = len(FollowUser.objects.filter(following=user))

    data = {'posts': posts,
            'profile': profile,
            'users': users,
            'comments': comments,
            'foll': foll,
            'like': like_posts_author,
    }

    if request.method == 'POST':
        data = request.POST
        obj = Comment.objects.create(author=profile, message=data['message'], post_id=data['post_id'])
        obj.save()
        return redirect(f'/#{data["post_id"]}')

    return render(request, 'index.html', context=data)


@login_required(login_url='/auth/login/')
def profile_view(request, a):
    user = MyUser.objects.filter(user=request.user).first()
    profile = MyUser.objects.filter(id=a).first()
    post = Post.objects.filter(author=profile)
    posts = len(Post.objects.filter(author=profile))
    foll = [i.following for i in FollowUser.objects.filter(follower=request.user.id)]

    followers = len(FollowUser.objects.filter(follower=profile))
    following = len(FollowUser.objects.filter(following=profile))

    data = {'post': post,
            'posts': posts,
            'user': user,
            'profile': profile,
            'foll': foll,
            'followers': followers,
            'following': following
            }

    return render(request, 'profile.html', context=data)


@login_required(login_url='/auth/login/')
def settings_view(request):
    return render(request, 'setting.html')
