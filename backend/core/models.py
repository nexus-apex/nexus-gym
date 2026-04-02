from django.db import models

class GymMember(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(blank=True, default="")
    phone = models.CharField(max_length=255, blank=True, default="")
    membership_type = models.CharField(max_length=50, choices=[("monthly", "Monthly"), ("quarterly", "Quarterly"), ("annual", "Annual"), ("day_pass", "Day Pass")], default="monthly")
    join_date = models.DateField(null=True, blank=True)
    expiry_date = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=50, choices=[("active", "Active"), ("expired", "Expired"), ("frozen", "Frozen")], default="active")
    emergency_contact = models.CharField(max_length=255, blank=True, default="")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.name

class FitnessClass(models.Model):
    name = models.CharField(max_length=255)
    instructor = models.CharField(max_length=255, blank=True, default="")
    class_type = models.CharField(max_length=50, choices=[("yoga", "Yoga"), ("crossfit", "CrossFit"), ("zumba", "Zumba"), ("pilates", "Pilates"), ("hiit", "HIIT"), ("spin", "Spin")], default="yoga")
    schedule = models.CharField(max_length=255, blank=True, default="")
    capacity = models.IntegerField(default=0)
    enrolled = models.IntegerField(default=0)
    duration_mins = models.IntegerField(default=0)
    status = models.CharField(max_length=50, choices=[("active", "Active"), ("cancelled", "Cancelled")], default="active")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.name

class Trainer(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(blank=True, default="")
    phone = models.CharField(max_length=255, blank=True, default="")
    specialization = models.CharField(max_length=255, blank=True, default="")
    experience_years = models.IntegerField(default=0)
    clients = models.IntegerField(default=0)
    rating = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    status = models.CharField(max_length=50, choices=[("active", "Active"), ("on_leave", "On Leave")], default="active")
    certification = models.CharField(max_length=255, blank=True, default="")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.name
