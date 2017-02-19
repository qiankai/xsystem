from __future__ import unicode_literals

from django.db import models
from employee.models import Employee

import uuid


class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    create_user = models.CharField(max_length=40)
    update_user = models.CharField(max_length=40)
    remark = models.TextField()


class Customer(BaseModel):
    identifier = models.CharField(max_length=20)
    customer_title = models.CharField(max_length=200)
    financial_account = models.CharField(max_length=200, blank=True, null=True)
    tax_account = models.CharField(max_length=200, blank=True, null=True)
    bank_name = models.CharField(max_length=200, blank=True, null=True)
    financial_address = models.CharField(max_length=200, blank=True, null=True)

    def __unicode__(self):
        return self.identifier + "," + self.customer_title


class CaseBaseInfo(BaseModel):
    MILESTONE_CHOICES = {
        1: 'set up the project',
        2: 'bid the project',
        3: 'sign contract',
        4: 'start implementation',
        5: 'check and accept',
        6: 'services ',
        0: 'closed',
    }
    identifier = models.CharField(max_length=20)
    case_title = models.CharField(max_length=200)
    contract_no = models.CharField(max_length=40, blank=True, null=True)
    pay_type = models.CharField(max_length=200, blank=True, null=True)
    current_budget = models.FloatField(blank=True, null=True)
    contract_total = models.FloatField(blank=True, null=True)
    contact_name = models.CharField(max_length=20, blank=True, null=True)
    contact_mobile = models.CharField(max_length=20, blank=True, null=True)
    case_address = models.CharField(max_length=256)
    case_deadline = models.DateField()
    milestone = models.SmallIntegerField(default=0, choices=MILESTONE_CHOICES.items())
    customer_title = models.ForeignKey("Customer", null=True, blank=True)

    def __unicode__(self):
        return self.identifier + "," + self.case_title


class BudgetRecord(BaseModel):
    budget = models.FloatField()
    case = models.ForeignKey("CaseBaseInfo", on_delete=models.CASCADE)

    def __unicode__(self):
        return str(self.budget) + "," + self.create_date.strftime("%Y-%m-%d")


class CaseBudget(BaseModel):
    TYPE_CHOICES = {
        1: 'selling expenses',
        2: 'implementation costs',
        0: 'miscellaneous expenses',
    }

    budget = models.FloatField()
    case = models.ForeignKey("CaseBaseInfo", on_delete=models.CASCADE)
    budget_type = models.SmallIntegerField(default=0, choices=TYPE_CHOICES.items())
    approved = models.BooleanField(default=False)
    cost_of_used = models.FloatField()
    open_ratio = models.FloatField()
    warning_tag = models.BooleanField(default=False)
    warning_level = models.FloatField()

    def __unicode__(self):
        return self.TYPE_CHOICES.get(self.budget_type) + "," + str(self.budget)


class CaseTeam(BaseModel):
    POSITION_CHOICES = {
        1: 'Development Manager',
        2: 'Project Manager',
        3: 'Designer',
        4: 'Developer',
    }

    RATIO_CHOICES = {
        1: '0.5',
        2: '0.75',
        3: '1',
    }
    case = models.ForeignKey("CaseBaseInfo", on_delete=models.CASCADE)

    member = models.ForeignKey("employee.Employee")
    position = models.SmallIntegerField(default=4, choices=POSITION_CHOICES.items())
    ratio = models.SmallIntegerField(default=1, choices=RATIO_CHOICES.items())
    enter_date = models.DateField()
    leave_date = models.DateField()
    workload = models.IntegerField()
    approved = models.BooleanField(default=False)

    def __unicode__(self):
        return self.case.identifier + "," + self.case.case_title + "," + self.member.real_name


class CasePayment(BaseModel):
    SEQUENCE_CHOICES = {
        1: 'first payment',
        2: 'second payment',
        3: 'third payment',
        4: 'forth payment',
        5: 'fifth payment',
    }
    case = models.ForeignKey("CaseBaseInfo", on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    to_pay_total = models.FloatField()
    to_pay_ratio = models.FloatField()
    to_pay_times = models.SmallIntegerField(default=1, choices=SEQUENCE_CHOICES.items())
    to_pay_date = models.DateField()
    pay_total = models.FloatField()
    pay_time = models.DateField()
    is_paid = models.BooleanField(default=False)

    def __unicode__(self):
        return self.case.identifier + ',' + str(self.to_pay_total)


class CaseCost(BaseModel):
    COST_TYPE_CHOICES = {
        1: 'catering expense',
        2: 'traffic expense (except air ticket)',
        3: 'air ticket expense',
        4: 'hotel expense',
        5: 'miscellaneous expenses'
    }

    case = models.ForeignKey("CaseBaseInfo", on_delete=models.CASCADE)
    total = models.FloatField()
    cost_type = models.SmallIntegerField(default=5, choices=COST_TYPE_CHOICES.items())
    occurrence_time = models.DateField()
    approve_sequence = models.CharField(max_length=500)
    current_approve = models.CharField(max_length=100)
    approve_record = models.TextField()
    is_fin = models.BooleanField(default=False)

    def __unicode__(self):
        return self.case.identifier + "," + self.COST_TYPE_CHOICES.get(self.cost_type) \
               + "," + str(self.total) + "," + self.occurrence_time.strftime("%Y-%m-%d")




















