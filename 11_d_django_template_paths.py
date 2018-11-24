from django.views.generic import ListView

class PostListView(ListView):
    template_name = 'post_list.html'  # post_list.html
