from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from django.core.management import CommandError

class Command(BaseCommand):
    help = 'Create or update admin users for the message board'

    def add_arguments(self, parser):
        parser.add_argument('--username', type=str, help='Username for the admin user')
        parser.add_argument('--email', type=str, help='Email for the admin user')
        parser.add_argument('--password', type=str, help='Password for the admin user')

    def handle(self, *args, **options):
        username = options.get('username') or 'admin'
        email = options.get('email') or 'admin@example.com'
        password = options.get('password') or 'admin123'

        try:
            # Check if user exists
            user, created = User.objects.get_or_create(
                username=username,
                defaults={
                    'email': email,
                    'is_staff': True,
                    'is_superuser': True,
                }
            )

            # Set password
            user.set_password(password)
            user.save()

            if created:
                self.stdout.write(
                    self.style.SUCCESS(f'✅ Successfully created admin user: {username}')
                )
            else:
                self.stdout.write(
                    self.style.SUCCESS(f'✅ Successfully updated admin user: {username}')
                )

            self.stdout.write(f'Username: {username}')
            self.stdout.write(f'Email: {email}')
            self.stdout.write(f'Password: {password}')
            self.stdout.write('🔐 Admin user is ready to access the admin panel!')

        except Exception as e:
            raise CommandError(f'❌ Error creating admin user: {e}')