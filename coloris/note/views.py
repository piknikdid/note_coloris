from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import TemplateView
from .forms import NoteForm
from rest_framework import viewsets
from .models import Note
from .serializers import NoteSerializer


def countText(value):
    words = value.text.split()
    count = {}
    for word in words :
        if word.lower() in count :
            count[word.lower()] += 1
        else:
            count[word.lower()] = 1
    return len(count)


class Index(TemplateView):
    template_name = 'note/index.html'




    def get(self,request):
        form = NoteForm()
        data = Note.objects.all()
        datac = list( i for i in data)

        d= sorted(datac,key=countText)

        return render(request, self.template_name, {'form':form, 'data': d})

    def post(self,request):
        form = NoteForm(request.POST)

        if form.is_valid():
            post = form.save(commit=False)

            post.save()
            text=form.cleaned_data['text']
            title= form.cleaned_data['title']
            return redirect('note:index')

        args = {'form':form, 'text':text}
        return  render(request, self.template_name, args)


class ApiNote(viewsets.ModelViewSet):
    queryset = Note.objects.all().order_by('pub_date')
    serializer_class = NoteSerializer
