from django.db import models


class ActivityLog(models.Model):
    PARTNER_CHOICES = [
        ('CIPRB', 'CIPRB'),
        ('PHD', 'PHD'),
        ('Bondhu', 'Bondhu'),
    ]
    partner = models.CharField(max_length=20, choices=PARTNER_CHOICES)
    district = models.CharField(max_length=255)
    upazila = models.CharField(max_length=255)
    activity_type = models.CharField(max_length=255)
    staff_name = models.CharField(max_length=255)
    beneficiary_count = models.IntegerField()

    def __str__(self):
        return f"{self.activity_type} by {self.staff_name}"
