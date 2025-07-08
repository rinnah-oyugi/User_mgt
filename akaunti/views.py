from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from django.contrib import messages

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False  # disable login until email verified
            user.save()

            uid = urlsafe_base64_encode(force_bytes(user.pk))
            token = default_token_generator.make_token(user)
            activation_link = request.build_absolute_uri(
                f'/verify/{uid}/{token}/'
            )

            subject = 'Verify your email'
            message = render_to_string('akaunti/activation_email.html', {
                'user': user,
                'activation_link': activation_link,
            })

            send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [user.email])
            messages.success(request, 'Account created! Check your email to verify it.')
            return redirect('login')
    else:
        form = UserRegisterForm()

    return render(request, 'akaunti/register.html', {'form': form})
from django.contrib.auth import get_user_model

def verify_email(request, uidb64, token):
    User = get_user_model()
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (User.DoesNotExist, ValueError, TypeError, OverflowError):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        messages.success(request, 'Your email has been verified! You can now log in.')
        return redirect('login')
    else:
        messages.error(request, 'Invalid or expired verification link.')
        return redirect('register')
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required
def profile(request):
    return render(request, 'akaunti/profile.html')
from django.contrib.auth.decorators import login_required

def dashboard(request):
    return render(request, 'akaunti/dashboard.html')


