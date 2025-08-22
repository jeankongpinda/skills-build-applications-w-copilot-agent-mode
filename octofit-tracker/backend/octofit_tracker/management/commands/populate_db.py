from django.core.management.base import BaseCommand
from octofit_tracker.models import Team, User, Activity, Workout, Leaderboard
from django.utils import timezone
import random

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Clear existing data
        Activity.objects.all().delete()
        User.objects.all().delete()
        Team.objects.all().delete()
        Workout.objects.all().delete()
        Leaderboard.objects.all().delete()

        # Teams
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        # Users
        marvel_heroes = ['Iron Man', 'Captain America', 'Black Widow', 'Hulk', 'Thor', 'Spider-Man']
        dc_heroes = ['Superman', 'Batman', 'Wonder Woman', 'Flash', 'Aquaman', 'Cyborg']

        marvel_users = [User.objects.create(name=hero, email=f"{hero.replace(' ', '').lower()}@marvel.com", team=marvel, is_superhero=True) for hero in marvel_heroes]
        dc_users = [User.objects.create(name=hero, email=f"{hero.replace(' ', '').lower()}@dc.com", team=dc, is_superhero=True) for hero in dc_heroes]

        # Activities
        activity_types = ['Running', 'Cycling']
        for user in marvel_users + dc_users:
            for activity_type in activity_types:
                Activity.objects.create(
                    user=user,
                    type=activity_type,
                    duration=random.randint(30, 120),
                    date=timezone.now()
                )

        # Workouts
        Workout.objects.create(name='Shield Training', description='Train like a S.H.I.E.L.D. agent.', suggested_for='marvel')
        Workout.objects.create(name='Stark Tech HIIT', description='High intensity interval training with Stark tech.', suggested_for='marvel')
        Workout.objects.create(name='Justice League Bootcamp', description='Bootcamp for Justice League members.', suggested_for='dc')
        Workout.objects.create(name='Speed Force Cardio', description='Cardio inspired by the Speed Force.', suggested_for='dc')
        Workout.objects.create(name='Universal Strength', description='Strength training for all heroes.', suggested_for='both')
        Workout.objects.create(name='Hero Recovery Yoga', description='Yoga for recovery and flexibility.', suggested_for='both')

        # Leaderboard
        marvel_points = sum([sum([a.duration for a in Activity.objects.filter(user=u)]) for u in marvel_users])
        dc_points = sum([sum([a.duration for a in Activity.objects.filter(user=u)]) for u in dc_users])
        Leaderboard.objects.create(team=marvel, points=marvel_points)
        Leaderboard.objects.create(team=dc, points=dc_points)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
