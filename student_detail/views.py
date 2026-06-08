from django.shortcuts import render, redirect
from .form import StudentForm
from .models import Student_d


def student_view(request):

    if request.method == 'POST':
        form = StudentForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('show')

    else:
        form = StudentForm()

    return render(request, 'student_detail/index.html', {'form': form})


def show(request):

    data = Student_d.objects.all()

    return render(request, 'student_detail/show.html', {'data': data})



def update(request, id):

    student = Student_d.objects.get(id=id)

    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)

        if form.is_valid():
            form.save()
            return redirect('show')

    else:
        form = StudentForm(instance=student)

    return render(request, 'student_detail/index.html', {'form': form})




def delete(request,id):
    data = Student_d.objects.get(id=id)
    data.delete()


    return redirect('show')
















     

