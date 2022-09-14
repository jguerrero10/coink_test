from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse

from coinkApp.forms import UserBasicForm
from coinkApp.models import UserBasic


def list_user_basic(request):
    users = UserBasic.objects.all()
    return render(request, 'users/index.ht.html', {'users': users})


def create_user_basic(request):
    context = dict()
    if request.method == 'POST':
        form = UserBasicForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Usuario registrado correctamente')
        else:
            messages.error(request, 'Error al registrar usuario. Intente nuevamente')
        return redirect(reverse('list-user-basic'))
    else:
        form = UserBasicForm()
        context['action'] = 'Crear'
        context['form'] = form
        return render(request, 'users/create_update.html', context)


def update_user_basic(request, id):
    context = dict()
    try:
        user = UserBasic.objects.get(id=id)
        if request.method == 'POST':
            form = UserBasicForm(request.POST, instance=user)
            if form.is_valid():
                form.save()
                messages.success(request, 'Usuario actualizado correctamente')
            else:
                messages.error(request, 'Error al actualizar usuario. Intente nuevamente')
            return redirect(reverse('list-user-basic'))
        else:
            form = UserBasicForm(instance=user)
            context['action'] = 'Actualizar'
            context['form'] = form
            return render(request, 'users/create_update.html', context)
    except ObjectDoesNotExist:
        messages.error(request, 'El usuario no se encuentra en la Base de datos. Por favor verifique e intente '
                                'nuevamente')
        return redirect(reverse('list-user-basic'))


def delete_user_basic(request, id):
    try:
        user = UserBasic.objects.get(id=id)
        user.delete()
        messages.success(request, f'Usuario {user} fue eliminado correctamente')
        return redirect(reverse('list-user-basic'))

    except ObjectDoesNotExist:
        messages.error(request, 'El usuario no se encuentra en la Base de datos. Por favor verifique e intente '
                                'nuevamente')
        return redirect(reverse('list-user-basic'))
