import uuid
from django.db import models
from django.utils.translation import ugettext_lazy as _


class LeadsModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    modified_at = models.DateTimeField(auto_now=True, blank=True)

    class Meta:
        abstract = True


class Status(models.TextChoices):
    OPEN = "Open", _("Open")
    PENDING = "Pending", _("Pending")
    COMPLETED = "Completed", _("Completed")


class Sheet(LeadsModel):
    pass


class Customer(LeadsModel):
    name = models.CharField(max_length=150, null=True)
    mobile = models.CharField(max_length=50, null=True)
    status = models.TextField(choices=Status.choices, null=True)
    address = models.CharField(max_length=150, null=True)
    industry = models.CharField(max_length=150, null=True)
    website = models.CharField(max_length=150, null=True)
    contacts = models.CharField(max_length=150, null=True)
    notes = models.TextField(null=True)
    pipelines = models.TextField(null=True)
    sheet_id = models.ForeignKey(Sheet, on_delete=models.CASCADE)
