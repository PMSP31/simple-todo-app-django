from django.views.generic import ListView
from todos.models import Todo

class IndexView(ListView):
    model = Todo
    template_name = 'index.html'
    context_object_name = 'todos'
    # ordering = ['-status']