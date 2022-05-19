from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView
from .forms import TodosForm
from .models import Todo

# Create your views here.
class TodosCreateView(CreateView):
    form_class = TodosForm
    template_name = 'todos/todos_create.html'

class TodosDeleteView(DeleteView):
    model = Todo
    success_url = reverse_lazy('index')

    def get(self, request, *args, **kwargs) :
        return self.post(request, *args, **kwargs)