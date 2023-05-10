from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from .models import Post
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import PostForm
from .forms import EditPostForm
from django.views.decorators.http import require_POST
from .forms import ContactForm
from .forms import CommentForm
from django.http import HttpResponseRedirect
from django.core.exceptions import PermissionDenied


class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by("-created_on")
    template_name = "index.html"
    paginate_by = 6

# post detail view
class PostDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by("-created_on")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "liked": liked,
                "commented": False,
                "comment_form": CommentForm()
            },
        )    

    def post(self, request, slug, *args, **kwargs):

        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by("-created_on")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
        else:
            comment_form = CommentForm()

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": True,
                "comment_form": comment_form,
                "liked": liked
            },
        )        
# create post view
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, user=request.user)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('home')
    else:
        form = PostForm(initial={'author': request.user})
    return render(request, 'create.html', {'form': form})

#edit post view
@login_required
def edit_post(request, slug):
    post = get_object_or_404(Post, slug=slug)

    if request.user == post.author:
        if request.method == 'POST':
            form = EditPostForm(request.POST, request.FILES, instance=post)
            if form.is_valid():
                post = form.save(commit=False)
                post.save()
                return redirect('post_detail', slug=post.slug)
        else:
            form = EditPostForm(instance=post)
        context = {'form': form, 'post': post}
        return render(request, 'edit_post.html', context)
    else:
        raise PermissionDenied

# delete post view
def delete_post(request, slug):
    post = get_object_or_404(Post, slug=slug)
    if request.user != post.author:
        raise PermissionDenied  # raise an exception if the user is not the author
    if request.method == 'POST':
        post.delete()
        return redirect('home')
    context = {
        'post': post,
    }
    return render(request, 'delete_post.html', context)

## Contact form view

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'contact_success.html')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})

## Likes View


class PostLike(View):
    
    def post(self, request, slug, *args, **kwargs):
        post = get_object_or_404(Post, slug=slug)
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return HttpResponseRedirect(reverse('post_detail', args=[slug]))
