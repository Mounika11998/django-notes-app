from django.shortcuts import render,redirect,get_object_or_404
from .models import Note
from .forms import NoteForm 

# Create your views here.
def note_list(request):
    notes=Note.objects.all()
    return render(request,'note_list.html',{'notes':notes})

def add_note(request):
    if request.method=="POST":
        form=NoteForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('note_list')
    else:
        form = NoteForm()
    return render(request, 'note_form.html', {'form': form})

def edit_note(request,pk):
    note = get_object_or_404(Note, pk=pk)
    if request.method=='POST':
        form=NoteForm(request.POST,instance=note)
        if form.is_valid():
            form.save()
            return redirect('note_list')
    else:
        form = NoteForm(instance=note)
    return render(request, 'edit_note.html', {'form': form})
def delete_note(request,pk):
    note=get_object_or_404(Note,pk=pk)
    if(request.method=='POST'):
        note.delete()
        return redirect('note_list')
    return render(request, 'confirm_delete.html', {'note': note})

