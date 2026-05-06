from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from django.db import connection
from pymongo import MongoClient

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Conexión directa a MongoDB para índices únicos
        client = MongoClient('localhost', 27017)
        db = client['octofit_db']
        db.users.drop()
        db.teams.drop()
        db.activities.drop()
        db.leaderboard.drop()
        db.workouts.drop()
        db.users.create_index([('email', 1)], unique=True)

        # Equipos
        teams = [
            {'name': 'Marvel', 'description': 'Team Marvel'},
            {'name': 'DC', 'description': 'Team DC'},
        ]
        team_ids = db.teams.insert_many(teams).inserted_ids

        # Usuarios
        users = [
            {'name': 'Iron Man', 'email': 'ironman@marvel.com', 'team': 'Marvel'},
            {'name': 'Captain America', 'email': 'cap@marvel.com', 'team': 'Marvel'},
            {'name': 'Batman', 'email': 'batman@dc.com', 'team': 'DC'},
            {'name': 'Wonder Woman', 'email': 'wonderwoman@dc.com', 'team': 'DC'},
        ]
        db.users.insert_many(users)

        # Actividades
        activities = [
            {'user': 'ironman@marvel.com', 'activity': 'Running', 'duration': 30},
            {'user': 'cap@marvel.com', 'activity': 'Cycling', 'duration': 45},
            {'user': 'batman@dc.com', 'activity': 'Swimming', 'duration': 60},
            {'user': 'wonderwoman@dc.com', 'activity': 'Yoga', 'duration': 50},
        ]
        db.activities.insert_many(activities)

        # Leaderboard
        leaderboard = [
            {'user': 'ironman@marvel.com', 'points': 100},
            {'user': 'cap@marvel.com', 'points': 90},
            {'user': 'batman@dc.com', 'points': 110},
            {'user': 'wonderwoman@dc.com', 'points': 95},
        ]
        db.leaderboard.insert_many(leaderboard)

        # Workouts
        workouts = [
            {'user': 'ironman@marvel.com', 'workout': 'Chest Day', 'suggestion': 'Bench Press'},
            {'user': 'cap@marvel.com', 'workout': 'Leg Day', 'suggestion': 'Squats'},
            {'user': 'batman@dc.com', 'workout': 'Cardio', 'suggestion': 'Treadmill'},
            {'user': 'wonderwoman@dc.com', 'workout': 'Flexibility', 'suggestion': 'Stretching'},
        ]
        db.workouts.insert_many(workouts)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
