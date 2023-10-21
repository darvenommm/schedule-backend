from django.shortcuts import render, redirect
from .models import User
from .forms import RegistrationForm

# registration
def register(request):
    form_errors = None
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            try:
                User.objects.create(user=user, name=request.POST['name'],
                                      surname=request.POST['surname'],
                                      email=request.POST['email']
                                      )
            except Exception as err:
                print('Нет пользователя: ', err)
            return redirect('/')
        form_errors = form.errors

    return render(
        request,
        'registration/register.html',
        context={
            'form': RegistrationForm(),
            'form_errors': form_errors,
        }
    )

from rest_framework.generics import GenericAPIView
from .serializers import*
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.decorators import permission_classes


@permission_classes((AllowAny, ))
class GithubSocialAuthView(GenericAPIView):

    serializer_class = GithubSocialAuthSerializer

    def post(self, request):
        """
        POST with "auth_token"
        Send an access token as from github to get user information
        """

        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = ((serializer.validated_data)['auth_token'])
        return Response(data, status=status.HTTP_200_OK)



