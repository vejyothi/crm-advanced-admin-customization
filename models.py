# from django.db import models

# Create your models here.
# from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
# Create your models here.
class roles(models.Model):
    ROLES_CHOICES=(
        ('Sales_rep','Sales_rep'),
        ('Sales_manager','Sales_manager'),
        ('Admin','Admin'),
    )
    roles_status=models.CharField(max_length=20,null=True,choices=ROLES_CHOICES)

    def _str_(self):
        return self.roles_status

class user_status(models.Model):
    USER_CHOICES=(
        ('Active','Active'),
        ('Inactive','Inactive'),
        ('Pending_approval','Pending_approval'),
    )
    status=models.CharField(max_length=20,null=True,choices=USER_CHOICES)
    def _str_(self):
        return self.status
    
class User(AbstractUser):
    name_title=models.CharField(max_length=200)
    name_first=models.CharField(max_length=100)
    name_middle=models.CharField(max_length=100)
    name_last=models.CharField(max_length=100)
    email=models.EmailField()
    password=models.CharField(max_length=50)
    User_Roles=models.ForeignKey(roles,null=True, on_delete=models.CASCADE)
    User_Status=models.ForeignKey(user_status,null=True, on_delete=models.CASCADE)

    def _str_(self):
        return self.name_title

class Contact_Status(models.Model):
    CONTACT_CHOICES=(
        ('Lead','Lead'),
        ('Opportunity','Opportunity'),
        ('Customer/won','Customer/won'),
        ('Archive','Archive'),
    )
    status=models.CharField(max_length=20,null=True,choices=CONTACT_CHOICES)
    def _str_(self):
        return self.status

class Contact(models.Model):
    contact_Title=models.CharField(max_length=200)
    contact_First=models.CharField(max_length=200)
    contact_Middle=models.CharField(max_length=200)
    contact_Last=models.CharField(max_length=200)
    lead_Refferal_Source=models.CharField(max_length=200)
    date_Of_Intial_Contact=models.DateTimeField()
    title=models.CharField(max_length=200)
    company=models.CharField(max_length=200)
    industry=models.CharField(max_length=200)
    address=models.CharField(max_length=200)
    address_street_1=models.CharField(max_length=200)
    address_street_2=models.CharField(max_length=200)
    address_City=models.CharField(max_length=200)
    address_State=models.CharField(max_length=200)
    adress_Zip=models.CharField(max_length=200)
    address_Country=models.CharField(max_length=200)
    phone=models.CharField(max_length=200)
    email=models.EmailField()
    status=models.ForeignKey(Contact_Status,null=True,on_delete=models.CASCADE)
    website=models.URLField()
    linkedIn_Profile=models.CharField(max_length=200)
    background_Inf=models.TextField()
    sales_Rep=models.OneToOneField(User, on_delete=models.CASCADE)
    rating=models.CharField(max_length=30)
    project_Type=models.CharField(max_length=200)
    project_Description=models.TextField()
    proposal_Due_Date=models.DateField()
    budget=models.FloatField()
    deliverables=models.CharField(max_length=200)  

    def _str_(self):
        return self.contact_Title


class task_status(models.Model):
    STATUS_CHOICES=(
        ('Pending','Pending'),
        ('Completed','Completed'),
    )
    status=models.CharField(max_length=20,choices=STATUS_CHOICES)
    def _str_(self):
        return self.status


class todo_type(models.Model):
    TYPE_CHOICES=(
        ('task','task'),
        ('meeting','meeting'),
    )
    type=models.CharField(max_length=20,choices=TYPE_CHOICES)
    def _str_(self):
        return self.type


class todo_desc(models.Model):
    DESC_CHOICES=(
        ('Follow Up Email','Follow Up Email'),
	    ('Phone Call','Phone Call'),
	    ('Lunch Meeting','Lunch Meeting'),
        ('Tech Demo','Tech Demo'),
	    ('Meetup','Meetup'),
	    ('Conference','Conference'),
	    ('Others','Others'),
    )
    description=models.CharField(max_length=20,choices=DESC_CHOICES)

    def _str_(self):
        return self.description


class Notes(models.Model):
    date = models.DateField()
    notes = models.CharField(max_length=200, null=True)
    is_New_Todo = models.CharField(max_length=200, null=True)
    Todo_Type_ID = models.ForeignKey(todo_type,null=True, on_delete=models.CASCADE)
    Todo_Desc_ID = models.ForeignKey(todo_desc,null=True, on_delete=models.CASCADE)
    Todo_Due_Date = models.DateField()
    Contact = models.ForeignKey(Contact,null=True, on_delete=models.CASCADE)
    Task_Status = models.ForeignKey(task_status,null=True, on_delete=models.CASCADE)
    Task_Update = models.CharField(max_length=200, null=True)
    Sales_Rep = models.CharField(max_length=200, null=True)
    def _str_(self):
        return self.notes
