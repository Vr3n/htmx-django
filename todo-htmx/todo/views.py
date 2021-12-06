from django.shortcuts import render
from .forms import TaskForm
from .models import Task


def home(request):
    if request.method == "GET":
        # retrieve the old tasks if our user is logged in
        if request.user.is_authenticated:
            tasks = Task.objects.filter(user=request.user)
        else:
            tasks = None
        # render the form
        form = TaskForm()
        # Return our home template.
        return render(
            request, "pages/home.html", {"form": form,
                                         "tasks": tasks, "errors": None}
        )
    # request method is POST
    else:
        # new
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            # we would only return our tasks components with the updated tasks
            tasks = Task.objects.filter(user=request.user)

            return render(
                request,
                "components/tasks.html",
                {
                    "form": TaskForm(),
                    "tasks": tasks,
                    "errors": None,
                },  # a new empty form, since we saved the posted one
            )

        # form is not valid, we have some kind of error
        else:
            errors = form.errors
            tasks = Task.objects.filter(user=request.user)
            # we would return only our tasks components with the old tasks, and the errors
            return render(
                request,
                "components/tasks.html",
                {
                    "form": form,
                    "tasks": tasks,
                    "errors": errors,
                },  # the posted form, since it didn't save
            )


def auth(request):
    return render(request, "components/auth.html")
