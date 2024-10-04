from django.shortcuts import render, redirect

# Login view for setting session
def login_session_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        request.session['username'] = username
        request.session['email'] = email
        return redirect('set_session')  # Redirect to Set Session page
    return render(request, 'login_session.html')  # Render login page for session

# Set Session view
def set_session_view(request):
    if 'username' in request.session:
        if request.method == 'POST':
            return redirect('session_created')  # Redirect to Session Created page
        return render(request, 'set_session.html', {'username': request.session['username']})
    return redirect('login_session')  # Redirect to login if session not set

# Session Created view
def session_created_view(request):
    if 'username' in request.session:
        return render(request, 'session_created.html', {'username': request.session['username']})
    return redirect('login_cookie')  # Redirect to login if session not set

# Login view for setting cookie
def login_cookie_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        request.session['username'] = username
        return redirect('set_cookie')  # Redirect to Set Cookie page
    return render(request, 'login_cookie.html')  # Render login page for cookie

# Set Cookie view
def set_cookie_view(request):
    if 'username' in request.session:
        if request.method == 'POST':
            mobile = request.POST.get('mobile')
            response = redirect('cookie_created')  # Redirect to Cookie Created page
            response.set_cookie('mobile', mobile)  # Set the cookie
            return response
        return render(request, 'set_cookie.html', {'username': request.session['username']})
    return redirect('login_cookie')  # Redirect to login if session not set

# Cookie Created view
def cookie_created_view(request):
    if 'username' in request.session and request.COOKIES.get('mobile'):
        return render(request, 'cookie_created.html', {
            'username': request.session['username'],
            'mobile': request.COOKIES.get('mobile')
        })
    return redirect('login_cookie')  # Redirect to login if session or cookie not set