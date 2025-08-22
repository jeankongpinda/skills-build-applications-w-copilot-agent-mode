from django.test import TestCase
from .models import User, Team, Activity, Workout, Leaderboard

class UserModelTest(TestCase):
    def test_create_user(self):
        team = Team.objects.create(name='Test Team')
        user = User.objects.create(name='Test User', email='test@octofit.com', team=team, is_superhero=True)
        self.assertEqual(user.name, 'Test User')
        self.assertEqual(user.team.name, 'Test Team')

class TeamModelTest(TestCase):
    def test_create_team(self):
        team = Team.objects.create(name='Test Team')
        self.assertEqual(team.name, 'Test Team')

class ActivityModelTest(TestCase):
    def test_create_activity(self):
        team = Team.objects.create(name='Test Team')
        user = User.objects.create(name='Test User', email='test@octofit.com', team=team, is_superhero=True)
        activity = Activity.objects.create(user=user, type='Running', duration=60, date='2025-08-22T00:00:00Z')
        self.assertEqual(activity.type, 'Running')
        self.assertEqual(activity.duration, 60)

class WorkoutModelTest(TestCase):
    def test_create_workout(self):
        workout = Workout.objects.create(name='Test Workout', description='Test Desc', suggested_for='both')
        self.assertEqual(workout.name, 'Test Workout')
        self.assertEqual(workout.suggested_for, 'both')

class LeaderboardModelTest(TestCase):
    def test_create_leaderboard(self):
        team = Team.objects.create(name='Test Team')
        leaderboard = Leaderboard.objects.create(team=team, points=100)
        self.assertEqual(leaderboard.team.name, 'Test Team')
        self.assertEqual(leaderboard.points, 100)
