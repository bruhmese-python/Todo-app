import operator
from django.shortcuts import redirect, render
from .models import Task
from .forms import ModelForm
# Create your views here.


# from django.views.generic import ListView
# from django.views.generic.detail import DetailView
# from django.views.generic.edit import DeleteView, UpdateView


# class TaskDetailView(ListView):
#     model = Task
#     template_name = 'Home.html'
#     context_object_name = 'todo'


# class TaskListView(DetailView):
#     model = Task
#     template_name = 'Home.html'
#     context_object_name = 'todo'


# class TaskUpdateView(UpdateView):
#     model = Task
#     template_name = 'Home.html'
#     context_object_name = 'todo'
#     fields = ('name', 'priority', 'date')

#     def get_success_url(request):
#         return reverse_lazy('viewdetails', kwargs={'pk': self.object.id})


# class TaskDeleteView(DeleteView):
#     model = Task
#     template_name = 'delete.html'
#     success_url = reverse_lazy('start')


def save(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        priority = request.POST.get('priority')
        date = request.POST.get('date')
        _obj = Task(name=name, priority=priority, date=date)
        _obj.save(request)
    return redirect('/')


def delete(request, id):
    _obj = Task.objects.get(id=id)
    _obj.delete()
    return redirect('/')


def details_update(request, id):
    obj = Task.objects.all()
    ordered = sorted(obj, key=operator.attrgetter('priority'))
    _obj = Task.objects.get(id=id)
    return render(request, 'Home.html', {'todo': ordered, 'localtodo': _obj, 'todoid': id, 'show_model': 1})


def viewdetails(request, id):
    obj = Task.objects.all()
    ordered = sorted(obj, key=operator.attrgetter('priority'))
    try:
        _obj = Task.objects.get(id=id)
    except:
        return handler404(request)
    return render(request, "Home.html", {'todo_task': _obj, 'todo': ordered, 'show_detail': 1})


def handler404(request, *args, **argv):
    template_name = "404.html"
    response = render(request, template_name)
    response.status_code = 404
    return response


def update(request, id):
    if request.method == 'POST':
        try:
            _obj = Task.objects.get(id=id)
        except:
            return handler404(request)
        form = ModelForm(request.POST or None, request.FILES, instance=_obj)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request, "Home.html", {'todo': _obj})


def start(request):
    obj = Task.objects.all()
    ordered = sorted(obj, key=operator.attrgetter('priority'))
    return render(request, "Home.html", {'todo': ordered})
