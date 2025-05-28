from django.shortcuts import render,redirect
from . models import Department,PositionList,EmpList
from . forms import dep_reg,position_reg,emp_reg

def index_page(request):
    return render(request,'main_home.html')

def dashboard(request):
    dept =Department.objects.count()
    posi = PositionList.objects.count()
    emp = EmpList.objects.count()
    context ={'dept':dept,'posi':posi,'emp':emp}
    return render(request,'dashboard_count.html',context)




def dept_data(request):
    data = Department.objects.all()
    context = {'data':data}
    return render(request,'base/department_templates/dept_dt.html',context)

def update_pg(request,pk):
    dept_id = Department.objects.get(id=pk)
    form = dep_reg(instance=dept_id)
    if request.method == 'POST':
        form =dep_reg(request.POST,instance=dept_id)
        if form .is_valid():
            form.save()
            return redirect("dept")
    context ={'form':form}
    return render(request,'base/department_templates/update_pg.html',context)

def delete_pg(request,pk):
    data = Department.objects.get(id=pk)
    if request.method == 'POST':
        data.delete()
        return redirect('dept')
    context ={'data':data}
    
    return render(request,'base/department_templates/delete_pg.html',context)


def create_dept(request):
    form = dep_reg()
    if request.method == 'POST':
        form = dep_reg(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dept')
    context ={'page':form}
    return render(request,'base/department_templates/save_dept_data.html',context)






def posi_data(request):
    data = PositionList.objects.all()
    context = {'data':data}
    return render(request,'base/postion_templates/posi_det.html',context)

def create_posi(request):
    form = position_reg()
    if request.method == 'POST':
        form = position_reg(request.POST)
        if form.is_valid():
            form.save()
            return redirect("position_data")
    context ={'form':form}
    return render(request,'base/postion_templates/save_posi.html',context)

def update_posi(request,pk):
    id = PositionList.objects.get(id=pk)
    form = position_reg(instance=id)
    
    if request.method =='POST':
        form = position_reg(request.POST,instance=id)
        if form.is_valid():
            form.save()
            return redirect('position_data')
    context ={'form':form}
    return render(request,'base/postion_templates/update_posi.html',context)    


def delete_posi(request,pk):
    data =PositionList.objects.get(id=pk)

    if request.method == 'POST':
        data.delete()
        return redirect('position_data')
    
    context ={'data':data}
    return render(request,'base/postion_templates/delete_posi.html',context)



def emp_data(request):
    data = EmpList.objects.all()
    context = {'data':data}
    return render(request,'base/employee_templates/emp_det.html',context)

def create_emp(request):
    form = emp_reg()
    if request.method == 'POST':
        form = emp_reg(request.POST)
        if form.is_valid():
            form.save()
            return redirect("emp_data")
    context ={'form':form}
    return render(request,'base/employee_templates/save_emp.html',context)

def update_emp(request,pk):
    id = EmpList.objects.get(id=pk)
    form = emp_reg(instance=id)
    
    if request.method =='POST':
        form = emp_reg(request.POST,instance=id)
        if form.is_valid():
            form.save()
            return redirect('emp_data')
    context ={'form':form}
    return render(request,'base/employee_templates/update_emp.html',context)    


def delete_emp(request,pk):
    data =EmpList.objects.get(id=pk)

    if request.method == 'POST':
        data.delete()
        return redirect('emp_data')
    
    context ={'data':data}
    return render(request,'base/employee_templates/delete_emp.html',context)
