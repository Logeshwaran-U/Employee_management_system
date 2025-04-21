
from django.db import models

class Department(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-updated', '-created']  # Existing ordering for Department

    def __str__(self):
        return self.name

class PositionList(models.Model):
    position = models.CharField(max_length=255)
    department = models.ForeignKey(Department,on_delete=models.SET_NULL, null=True, related_name='positions')
    description = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-updated', '-created']  # Existing ordering for PositionList
        unique_together = ('position', 'department')

    def __str__(self):
        return self.position

class EmpList(models.Model):
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ]

    COUNTRY_CHOICES = [
        ('IN', '+91'),  # India
        ('US', '+1'),   # United States
        ('AU', '+61'),  # Australia
        ('CA', '+1'),   # Canada
        ('UK', '+44'),  # United Kingdom
        # Add more countries as needed
    ]

    name = models.CharField(max_length=255)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    birthday = models.DateField()
    email = models.EmailField(unique=True)
    country_code = models.CharField(max_length=2, choices=COUNTRY_CHOICES)  # Country code
    contact_number = models.CharField(max_length=15)  # Adjust as necessary
    department = models.ForeignKey(Department,on_delete=models.SET_NULL, null=True, related_name='employees')
    position = models.ForeignKey(PositionList, on_delete=models.SET_NULL, null=True, related_name='employees')
    date_hired = models.DateField()
    monthly_salary = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.BooleanField(default=True)  # Changed to BooleanField
    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True)


    class Meta:
        ordering = ['name']  

    def __str__(self):
        return self.name
