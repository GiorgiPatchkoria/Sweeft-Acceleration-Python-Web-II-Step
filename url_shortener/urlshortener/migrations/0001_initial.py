from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='URL',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('click_times', models.PositiveIntegerField(default=0)),
                ('long_url', models.URLField(max_length=250)),
                ('short_url', models.CharField(blank=True, max_length=7, unique=True)),
                ('premium_short_url', models.CharField(max_length=25, unique=True)),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
    ]