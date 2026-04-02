from django.contrib import admin
from .models import GymMember, FitnessClass, Trainer

@admin.register(GymMember)
class GymMemberAdmin(admin.ModelAdmin):
    list_display = ["name", "email", "phone", "membership_type", "join_date", "created_at"]
    list_filter = ["membership_type", "status"]
    search_fields = ["name", "email", "phone"]

@admin.register(FitnessClass)
class FitnessClassAdmin(admin.ModelAdmin):
    list_display = ["name", "instructor", "class_type", "schedule", "capacity", "created_at"]
    list_filter = ["class_type", "status"]
    search_fields = ["name", "instructor", "schedule"]

@admin.register(Trainer)
class TrainerAdmin(admin.ModelAdmin):
    list_display = ["name", "email", "phone", "specialization", "experience_years", "created_at"]
    list_filter = ["status"]
    search_fields = ["name", "email", "phone"]
