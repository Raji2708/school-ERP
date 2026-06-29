from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import Register
from .models import Circular
from .models import Employee
from .models import Allocation
from .models import Assignmentx
from .models import ImageUpload
from .models import Student
from .models import Staff
from django.shortcuts import render, redirect
from .forms import UploadForm
from .forms import Studentbio
from .forms import Staffbio

def index(request):
  student = Register.objects.all().values()
  template = loader.get_template('staff.html')
  context = {
    'student': student,
  }
  return HttpResponse(template.render(context, request))
  
def add(request):
  template = loader.get_template('adminn.html')
  return HttpResponse(template.render({}, request))

def principal(request):
  template = loader.get_template('principal.html')
  return HttpResponse(template.render({}, request))

def addadminn(request):
  template = loader.get_template('addadmin.html')
  return HttpResponse(template.render({}, request))

def addstafff(request):
  template = loader.get_template('addstaff.html')
  return HttpResponse(template.render({}, request))

def login(request):
  template = loader.get_template('login.html')
  return HttpResponse(template.render({}, request))

def studentlogin(request):
  template = loader.get_template('studentlogin.html')
  return HttpResponse(template.render({}, request))

def addcircular(request):
  template = loader.get_template('circular.html')
  return HttpResponse(template.render({}, request))

def viewstudent(request):
  student = Register.objects.all().values()
  template = loader.get_template('staff.html')
  context = {
    'student': student,
  }
  return HttpResponse(template.render(context, request))
  
def addrecord(request):
  a = request.POST['name']
  b = request.POST['ids']
  c = request.POST['age']
  d = request.POST['classs']
  e = request.POST['fee']
  f = request.POST['balance']
  g = request.POST['percent']
  member = Register(name=a, ids=b, age=c, classs=d, fee=e, balance=f, percent=g)
  member.save()
  return HttpResponseRedirect(reverse('add'))

def addstaff(request):
  a = request.POST['name']
  b = request.POST['password']
  c = request.POST['designation']
  staff = Employee(name=a, password=b, designation=c)
  staff.save()
  return HttpResponseRedirect(reverse('addstafff'))

def addadmin(request):
  a = request.POST['name']
  b = request.POST['password']
  c = request.POST['designation']
  adminn = Employee(name=a, password=b, designation=c)
  adminn.save()
  return HttpResponseRedirect(reverse('addadminn'))


def addrecordcircular(request):
  a = request.POST['circular']
  info = Circular(circular=a)
  info.save()
  return HttpResponseRedirect(reverse('addcircular'))


def viewadmin(request):
  admin = Employee.objects.filter(designation="admin")
  template = loader.get_template('viewadmin.html')
  context = {
    'admin': admin,
  }
  return HttpResponse(template.render(context, request))

def viewstaff(request):
  staff = Employee.objects.filter(designation="staff")
  template = loader.get_template('viewstaff.html')
  context = {
    'staff': staff,
  }
  return HttpResponse(template.render(context, request))

def loginrecord(request):
  a = request.POST['name']
  b = request.POST['password']
  member = Employee.objects.filter(name=a,password=b).first()
  if member:
    if member.designation=="staff":
      student = Register.objects.all().values()
      template = loader.get_template('staff.html')
      context = {
      'student': student,
      }
      return HttpResponse(template.render(context, request))
    if member.designation=="admin":
      template = loader.get_template('adminn.html')
      return HttpResponse(template.render({}, request))
    if member.designation=="principal":
      template = loader.get_template('principal.html')
      return HttpResponse(template.render({}, request))

def studentloginrecord(request):
  a = request.POST['name']
  b = request.POST['ids']
  student = Register.objects.filter(name=a,ids=b).values()
  inform = Circular.objects.all().values()
  template = loader.get_template('student.html')
  context = {
    'student': student,
    'inform': inform,
  }
  return HttpResponse(template.render(context, request))

def change(request):
  employe = Employee.objects.all().values()
  template = loader.get_template('employeedetails.html')
  context = {
    'employe': employe,
  }
  return HttpResponse(template.render(context, request))
  

def changedesign(request):
  template = loader.get_template('changedesignation.html')
  return HttpResponse(template.render({}, request))

def changing(request):
  a = request.POST['id']
  b = request.POST['name']
  c = request.POST['designation']
  employe = Employee(id=a, name=b, designation=c)
  Employee.objects.filter(id=a).update(designation=c)
  return HttpResponseRedirect(reverse('login'))

def delete(request):
  template = loader.get_template('delete.html')
  return HttpResponse(template.render({}, request))

def deletex(request):
  a = request.POST['id']
  b = request.POST['name']
  employe = Employee(id=a,name=b)
  Employee.objects.filter(id=a,name=b).delete()
  return HttpResponseRedirect(reverse('login'))
  
def stafflogin(request):
  template = loader.get_template('stafflogin.html')
  return HttpResponse(template.render({}, request))

def staffloginn(request):
  a = request.POST['name']
  b = request.POST['password']
  person = Employee.objects.filter(name=a,password=b).first()
  if person:
    if person.designation == "staff":
      staff = Allocation.objects.filter(staffname=a).first()
      if staff:
        x=staff.stdid1
        y=staff.stdid2
        alloc=Register.objects.filter(id__in=[x,y])
        assign=Assignmentx.objects.filter(id__in=[x,y])
        template = loader.get_template('staffloginn.html')
        context = {
            'alloc':alloc,
            'assign':assign
        }
        return HttpResponse(template.render(context, request))

def allocate(request):
  template = loader.get_template('allocate.html')
  return HttpResponse(template.render({}, request))

def allocatee(request):
  a = request.POST['staffname']
  b = request.POST['stdid1']
  c = request.POST['stdid2']
  staff = Allocation(staffname=a,stdid1=b,stdid2=c)
  staff.save()
  return HttpResponseRedirect(reverse('allocate'))

def assign(request):
  template = loader.get_template('assignment.html')
  return HttpResponse(template.render({}, request))

def assignment(request):
  a = request.POST['name']
  b = request.POST['informs']
  messagee = Assignmentx(name=a,assignment=b)
  messagee.save()
  return HttpResponseRedirect(reverse('assign'))

def upload_image(request):
  if request.method == 'POST':
    form = UploadForm(request.POST, request.FILES)
    if form.is_valid():
      form.save()
      return redirect('success')
  else:
    form = UploadForm()
  return render(request, 'upload.html', {'form': form})

def success(request):
  return render(request, 'success.html')

def view_images(request):
    images = ImageUpload.objects.all()
    return render(request, 'gallery.html', {'images': images})

def upload_imagestd(request):
  if request.method == 'POST':
    form = Studentbio(request.POST, request.FILES)
    if form.is_valid():
      form.save()
      return redirect('successstd')
  else:
    form = Studentbio()
  return render(request, 'uploadstd.html', {'form': form})

def successstd(request):
  return render(request, 'successstd.html')

def view_imagesstd(request):
    images = Student.objects.all()
    return render(request, 'gallerystd.html', {'images': images})

def upload_imagex(request):
  if request.method == 'POST':
    form = Staffbio(request.POST, request.FILES)
    if form.is_valid():
      form.save()
      return redirect('successx')
  else:
    form = Staffbio()
  return render(request, 'uploadx.html', {'form': form})

def successx(request):
  return render(request, 'successx.html')

def view_imagesx(request):
    images = Staff.objects.all()
    return render(request, 'galleryx.html', {'images': images})