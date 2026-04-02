from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from core.models import GymMember, FitnessClass, Trainer
from datetime import date, timedelta
import random


class Command(BaseCommand):
    help = 'Seed NexusGym with demo data'

    def handle(self, *args, **kwargs):
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser('admin', 'admin@nexusgym.com', 'Admin@2024')
            self.stdout.write(self.style.SUCCESS('Admin user created'))

        if GymMember.objects.count() == 0:
            for i in range(10):
                GymMember.objects.create(
                    name=["Rajesh Kumar","Priya Sharma","Amit Patel","Deepa Nair","Vikram Singh","Ananya Reddy","Suresh Iyer","Meera Joshi","Karthik Rao","Fatima Khan"][i],
                    email=f"demo{i+1}@example.com",
                    phone=f"+91-98765{43210+i}",
                    membership_type=random.choice(["monthly", "quarterly", "annual", "day_pass"]),
                    join_date=date.today() - timedelta(days=random.randint(0, 90)),
                    expiry_date=date.today() - timedelta(days=random.randint(0, 90)),
                    status=random.choice(["active", "expired", "frozen"]),
                    emergency_contact=f"Sample {i+1}",
                )
            self.stdout.write(self.style.SUCCESS('10 GymMember records created'))

        if FitnessClass.objects.count() == 0:
            for i in range(10):
                FitnessClass.objects.create(
                    name=f"Sample FitnessClass {i+1}",
                    instructor=f"Sample {i+1}",
                    class_type=random.choice(["yoga", "crossfit", "zumba", "pilates", "hiit", "spin"]),
                    schedule=f"Sample {i+1}",
                    capacity=random.randint(1, 100),
                    enrolled=random.randint(1, 100),
                    duration_mins=random.randint(1, 100),
                    status=random.choice(["active", "cancelled"]),
                )
            self.stdout.write(self.style.SUCCESS('10 FitnessClass records created'))

        if Trainer.objects.count() == 0:
            for i in range(10):
                Trainer.objects.create(
                    name=["Rajesh Kumar","Priya Sharma","Amit Patel","Deepa Nair","Vikram Singh","Ananya Reddy","Suresh Iyer","Meera Joshi","Karthik Rao","Fatima Khan"][i],
                    email=f"demo{i+1}@example.com",
                    phone=f"+91-98765{43210+i}",
                    specialization=f"Sample {i+1}",
                    experience_years=random.randint(1, 100),
                    clients=random.randint(1, 100),
                    rating=round(random.uniform(1000, 50000), 2),
                    status=random.choice(["active", "on_leave"]),
                    certification=f"Sample {i+1}",
                )
            self.stdout.write(self.style.SUCCESS('10 Trainer records created'))
