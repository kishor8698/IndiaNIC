from django.shortcuts import render
from employee_app.models import Employee, EmployeeAttendanace
from django.http import JsonResponse
import json
from django.utils import timezone
from datetime import datetime

def save_employee(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')
        department = request.POST.get('department')
        if not name:
            return JsonResponse({'status': "error", "message": "Name field is mandatory."})
        if not email:
            return JsonResponse({'status': "error", "message": "Email field is mandatory."})
        if not mobile:
            return JsonResponse({'status': "error", "message": "Mobile field is mandatory."})
        if not department:
            return JsonResponse({'status': "error", "message": "Department field is mandatory."})

        email_exist = Employee.objects.filter(email=email).first()
        if email_exist:
            return JsonResponse({'status': "error", "message": "Email already exist in database"})
        # Create and save the employee object
        employee = Employee(name=name, email=email, mobile=mobile, department=department)
        employee.save()
        data={"name": name,"email": email, "mobile": mobile, "department": department,"emp_id": employee.id}
        return JsonResponse({'status': "success", "message": "Employee Created successfully.", "data": data})
def list_of_employees(request):
    employee = Employee.objects.all()
    return render(request, 'add_employee.html', {"data": employee})

def delete_employee(request):
    employee = Employee.objects.filter(id=request.POST.get('emp_id')).first()
    if employee:
        emp_id = employee.id
        employee.delete()
        return JsonResponse({'status': "success", "message": "Employee deleted successfully.", "data": {"emp_id": emp_id}})
    return JsonResponse({'status': "error", "message": "Record does not exist."})

def present_employee(request):
    employee_query = EmployeeAttendanace.objects.filter(employee_id=request.POST.get('emp_id')).first()
    true_or_false = json.loads(request.POST.get('is_present'))
    if employee_query:
        employee_query.is_present = true_or_false
        employee_query.save()
        return JsonResponse({'status': "success", "message": "Made as present.", "data":request.POST.get('is_present')})
    employee_query = EmployeeAttendanace(employee_id=request.POST.get('emp_id'), is_present=true_or_false)
    employee_query.save()
    return JsonResponse({'status': "error", "message": "Made as absent.", "data": request.POST.get('is_present')})

def todays_attendance(request):
    today = timezone.now().date()
    # Filter records created today
    todays_records = EmployeeAttendanace.objects.select_related("employee").filter(created_at__date=today).all()
    return render(request, 'today_attendance.html', {"todays_records": todays_records})

def all_attendance_employee(request):
    # Filter records created today
    all_attendance_employee = EmployeeAttendanace.objects.select_related("employee").all()
    return render(request, 'all_attendance_employee.html', {"all_attendance_employee": all_attendance_employee})


def edit_employee(request):
    employee = Employee.objects.filter(id=request.POST.get('emp_id')).first()
    if employee:
        updated_data = {}
        updated_data["name"] =  request.POST.get("name")
        updated_data["email"] =  request.POST.get("email")
        updated_data["mobile"] = request.POST.get("mobile")
        updated_data["department"] = request.POST.get("department")
        updated_data["emp_id"] = request.POST.get('emp_id')

        employee.name = request.POST.get("name")
        employee.email = request.POST.get("email")
        employee.mobile = request.POST.get("mobile")
        employee.department = request.POST.get("department")
        employee.save()
        return JsonResponse({'status': "success", "message": "Employee updated successfully.","updated_data":updated_data})
    return JsonResponse({'status': "error", "message": "Record does not exist."})