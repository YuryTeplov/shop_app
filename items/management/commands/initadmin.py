from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = "adding admin user with login admin and the same password"

    def handle(self, *args, **options):
        User.objects.create_superuser('admin', 'admin@admin.admin', 'admin')
