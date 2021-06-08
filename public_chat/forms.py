from django import forms
from .models import PublicChatRoom, PublicChatRoomMessage

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class JoinChatRoomForm(forms.Form):
    room = forms.ModelChoiceField(queryset=PublicChatRoom.objects.all(),widget=forms.HiddenInput)

class CreateRoomForm(forms.ModelForm):
    #joiners = forms.ModelMultipleChoiceField(queryset=User.objects.all())
    class Meta:
        model = PublicChatRoom
        fields = ['title','joiners'] 

class CreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username']