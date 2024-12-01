from django.shortcuts import render, redirect, get_object_or_404
from .forms import ImageForm
from .models import Image

# Home view: Display images
def home(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ImageForm()
    images = Image.objects.all()
    return render(request, 'myapp/home.html', {'form': form, 'images': images})

# Delete view
def delete_image(request, pk):
    img = get_object_or_404(Image, pk=pk)
    img.delete()
    return redirect('home')

# Edit view
def edit_image(request, pk):
    img = get_object_or_404(Image, pk=pk)
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES, instance=img)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ImageForm(instance=img)
    return render(request, 'myapp/edit_image.html', {'form': form, 'image': img})
