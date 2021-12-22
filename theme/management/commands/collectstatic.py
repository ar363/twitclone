from django.core.management import call_command
from django.contrib.staticfiles.management.commands.collectstatic import (
    Command as CollectStaticCommand,
)


class Command(CollectStaticCommand):
    def add_arguments(self, parser):
        
        parser.add_argument(
            '--skiptw',
            action='store_true',
            help='Skip tailwind build',
        )

        return super().add_arguments(parser)

    def handle(self, *args, **options):
        if options['skiptw']:
            call_command("tailwind", "build")
        
        super().handle(*args, **options)