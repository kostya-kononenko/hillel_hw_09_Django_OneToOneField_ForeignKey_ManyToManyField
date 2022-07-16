from django.contrib.auth.models import User
from django.core.management.base import BaseCommand


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('user_id', nargs='+', type=str, help='User ID')

    def handle(self, *args, **kwargs):
        users_ids = (kwargs['user_id'])
        if User.objects.all().filter(id__in=users_ids, is_superuser=True):
            self.stdout.write('You cannot delete superuser')
        else:
            User.objects.all().filter(id__in=users_ids).delete()
            self.stdout.write('User with entered ID was delete successfully')
