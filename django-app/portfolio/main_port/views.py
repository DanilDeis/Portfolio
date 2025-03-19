from django.contrib.sites import requests
from django.http import HttpRequest
from django.shortcuts import render, redirect
from .forms import UserBioForm
from .utils import send_telegram_message
def main_port_index(request: HttpRequest):
    return render(request, 'main_port/main_list_1.html')  # Убедитесь, что шаблон существует


def about_me_index(request):
    return render(request, 'main_port/about_me.html')


# def contact_index(request):
#     context = {
#         "form": UserBioForm(),
#     }
#     return render(request, 'main_port/data_prof.html', context=context)





def contact_index(request):
    if request.method == 'POST':
        form = UserBioForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            topic = form.cleaned_data['topic']
            text = form.cleaned_data['text']

            # Формируем сообщение для отправки
            message = f"Новое сообщение от {name} ({email})\nТема: {topic}\nСообщение: {text}"

            # Отправляем сообщение в Telegram
            chat_id = "877631642"  # Замените на ваш chat_id
            send_telegram_message(chat_id, message)
            return render(request, 'main_port/trash.html')
    else:
        form = UserBioForm()

    return render(request, 'main_port/data_prof.html', {'form': form})
