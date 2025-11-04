from django.shortcuts import render

# ✅ Home Page
def soft_view(request):
    return render(request, 'soft.html')

# ✅ About Page
def about_view(request):
    return render(request, 'about.html')

# ✅ Menu Page
def menu_view(request):
    return render(request, 'menu.html')

# ✅ Contact Page
def contact_view(request):
    return render(request, 'contact.html')

