from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from .models import PublicChatRoom, PublicChatRoomMessage
from .forms import JoinChatRoomForm, CreateRoomForm, CreationForm 
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden, request
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin

from django.views.generic.edit import CreateView, FormView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView, UpdateView
from django.db.models import Q

from django.contrib.auth import authenticate, login

User = get_user_model()


class CreateRoomView(CreateView):

    template_name = 'create_room.html'
    form_class = CreateRoomForm
    success_url = reverse_lazy('UsersListView')
    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.owner = self.request.user        
        self.object.save()   
        form.save_m2m() # important to save many-to-many choices   
        return redirect(self.success_url)

    # def get(self, request, *args, **kwargs):
    #     context = {'form': CreateRoomForm()}
    #     return render(request, 'create_room.html', context)

    # def post(self, request, *args, **kwargs):
    #     form = CreateRoomForm(request.POST)
    #     if form.is_valid():
    #         room = form.save(commit=False)
    #         room.owner = self.request.user
    #         room.save()
    #         return redirect(reverse_lazy('JoinerRoomList'))
    #     return render(request, 'create_room.html', {'form': form})


class UsersListView(LoginRequiredMixin, ListView):
    model = User
    template_name = 'users_list.html'


# class JoinerRoomListView(LoginRequiredMixin, ListView):
#     model = PublicChatRoom
#     template_name = 'list.html'
#     def get_queryset(self):
#         qs = super().get_queryset()
#         # print (qs)
        
#         return qs.filter(Q(owner__in=[self.request.user]))

 
class JoinerRoomDetailView(DetailView):
    model = PublicChatRoom
    template_name = 'detail.html'
    def get_queryset(self):
        qs = super().get_queryset()
        qs.filter(joiners__in=[self.request.user])
        return qs
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # get course object
        room = self.get_object()
        context['messages'] = PublicChatRoomMessage.objects.filter(room=room).order_by('-time_stamp')[:5:-1]
        
        return context

# def JoinerRoomDetailView(request, room_id):
#     room = PublicChatRoom.objects.get(id=room_id)
#     return render(request,'deta.html',{'room':room})

# class JoinerRoomDetailView(DetailView):
#     model = PublicChatRoom
#     template_name = 'detail.html'

class RoomDeleteView(DeleteView):
    model = PublicChatRoom 
    #template_name = 'users_list.html'
    success_url =reverse_lazy('UsersListView')

    # the get fuction will get rid of delete confirmation
    def get(self, *args, **kwargs):
        return self.post(*args, **kwargs)


class RoomJoinersUpdateView(UpdateView):
    model = PublicChatRoom
    template_name = 'update.html'
    fields = ["joiners"]
    success_url =reverse_lazy("UsersListView")

class RegistrationView(CreateView):
    template_name = 'registration.html'
    form_class = CreationForm
    success_url = reverse_lazy('UsersListView')
    def form_valid(self, form):
        result = super().form_valid(form)
        cd = form.cleaned_data
        user = authenticate(username=cd['username'],password=cd['password1'])
        login(self.request, user)
        return result