from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('urlshortener', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='url',
            name='premium_short_url',
        ),
    ]