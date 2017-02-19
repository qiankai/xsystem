from __future__ import unicode_literals

import uuid
from django.db import models
from django.contrib.auth.models import User,AbstractUser
from django.db.models.signals import post_save


class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    create_user = models.CharField(max_length=40)
    update_user = models.CharField(max_length=40)
    remark = models.TextField()

    class Meta:
        abstract = True


class Employee(BaseModel):
    SEX_CHOICES = {
        1: 'boy',
        2: 'girl',
    }

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    real_name = models.CharField(max_length=200)
    work_no = models.CharField(max_length=20)
    talk_user_id = models.CharField(max_length=200, blank=True, null=True, editable=False)
    mobile = models.CharField(max_length=20, blank=True, null=True)
    sex = models.SmallIntegerField(default=1, choices=SEX_CHOICES.items())
    birth = models.DateField(blank=True, null=True)
    # picture = models.ImageField(upload_to="Image/", blank=True, null=True)
    address = models.CharField(max_length=256, blank=True)
    emergent_name = models.CharField(max_length=20, blank=True)
    emergent_mobile = models.CharField(max_length=20, blank=True)
    position = models.CharField(max_length=20, blank=True)
    level = models.CharField(max_length=20, blank=True)
    last_year_degree = models.CharField(max_length=20, blank=True)
    last_year_gross = models.CharField(max_length=20, blank=True)
    emp_related_dt = models.ForeignKey("Department", null=True)

    def __unicode__(self):
        return self.real_name

    def save(self, *args, **kwargs):
        if not self.pk:
            try:
                p = Employee.objects.get(user=self.user)
                self.pk = p.pk
            except Employee.DoesNotExist:
                pass

        super(Employee, self).save(*args, **kwargs)


def create_user_profile(sender, instance, created, **kwargs):
    if created:
        profile = Employee()
        profile.user = instance
        profile.save()


post_save.connect(create_user_profile, sender=User)


class Department(BaseModel):
    dt_name = models.CharField(max_length=200)
    talk_id = models.CharField(max_length=200, blank=True)

    def __unicode__(self):
        return self.dt_name


class TalkRecord(BaseModel):
    tr_related_emp = models.ForeignKey("Employee")
    tr_title = models.CharField(max_length=200)
    tr_content = models.TextField()

    def __unicode__(self):
        return self.tr_title


class PositionRecord(BaseModel):
    pr_title = models.CharField(max_length=200)
    pr_related_emp = models.ForeignKey("Employee")

    def __unicode__(self):
        return self.pr_title + "," + self.create_date.strftime("%Y-%m-%d")


class LevelRecord(BaseModel):
    lr_title = models.CharField(max_length=200)
    lr_related_emp = models.ForeignKey("Employee")

    def __unicode__(self):
        return self.lr_title + "," + self.create_date.strftime("%Y-%m-%d")


class DegreeAndGrossRecord(BaseModel):
    dgr_mark_year = models.CharField(max_length=20)
    dgr_degree = models.CharField(max_length=20)
    dgr_gross = models.CharField(max_length=20)

    def __unicode__(self):
        return self.dgr_mark_year + "," + self.dgr_degree + "," + self.dgr_gross
