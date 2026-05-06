from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from .models import User, Team, Activity, Workout

class UserTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpass')

    def test_user_creation(self):
        self.assertEqual(User.objects.count(), 1)

class TeamTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.team = Team.objects.create(name='Team A')
        self.team.members.add(self.user)

    def test_team_creation(self):
        self.assertEqual(Team.objects.count(), 1)

class ActivityTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.activity = Activity.objects.create(user=self.user, type='run', duration=30, calories_burned=200, date='2024-01-01')

    def test_activity_creation(self):
        self.assertEqual(Activity.objects.count(), 1)

class WorkoutTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.workout = Workout.objects.create(name='Pushups', description='Do pushups', difficulty='Easy')

    def test_workout_creation(self):
        self.assertEqual(Workout.objects.count(), 1)
