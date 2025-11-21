from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from djongo import models

# Define models for teams, activities, leaderboard, workouts
class Team(models.Model):
    name = models.CharField(max_length=100, unique=True)
    class Meta:
        app_label = 'octofit_tracker'

class Activity(models.Model):
    user = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    duration = models.IntegerField()
    team = models.CharField(max_length=100)
    class Meta:
        app_label = 'octofit_tracker'

class Leaderboard(models.Model):
    user = models.CharField(max_length=100)
    team = models.CharField(max_length=100)
    points = models.IntegerField()
    class Meta:
        app_label = 'octofit_tracker'

class Workout(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    difficulty = models.CharField(max_length=50)
    class Meta:
        app_label = 'octofit_tracker'

User = get_user_model()

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Clear existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Create teams
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        # Create users
        users = [
            User.objects.create_user(username='ironman', email='ironman@marvel.com', password='password'),
            User.objects.create_user(username='captainamerica', email='cap@marvel.com', password='password'),
            User.objects.create_user(username='batman', email='batman@dc.com', password='password'),
            User.objects.create_user(username='superman', email='superman@dc.com', password='password'),
        ]

        # Create activities
        Activity.objects.create(user='ironman', type='Running', duration=30, team='Marvel')
        Activity.objects.create(user='captainamerica', type='Cycling', duration=45, team='Marvel')
        Activity.objects.create(user='batman', type='Swimming', duration=60, team='DC')
        Activity.objects.create(user='superman', type='Yoga', duration=20, team='DC')

        # Create leaderboard
        Leaderboard.objects.create(user='ironman', team='Marvel', points=100)
        Leaderboard.objects.create(user='captainamerica', team='Marvel', points=90)
        Leaderboard.objects.create(user='batman', team='DC', points=95)
        Leaderboard.objects.create(user='superman', team='DC', points=110)

        # Create workouts
        Workout.objects.create(name='Hero HIIT', description='High intensity interval training for heroes.', difficulty='Hard')
        Workout.objects.create(name='Power Yoga', description='Yoga for strength and flexibility.', difficulty='Medium')
        Workout.objects.create(name='Speed Run', description='Endurance running workout.', difficulty='Hard')
        Workout.objects.create(name='Recovery Stretch', description='Stretching for recovery.', difficulty='Easy')

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
