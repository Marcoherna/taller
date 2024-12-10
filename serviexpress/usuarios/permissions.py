from functools import wraps
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import redirect

def rol_requerido(roles_permitidos):
    def decorator(view_func):
        @wraps(view_func)
        def wrapper(request, *args, **kwargs):
            if request.user.is_authenticated and request.user.rol in roles_permitidos:
                return view_func(request, *args, **kwargs)
            return redirect('acceso_denegado')
        return wrapper
    return decorator