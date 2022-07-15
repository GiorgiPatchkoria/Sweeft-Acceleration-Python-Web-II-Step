from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('urlshortener', '0002_remove_url_premium_short_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='url',
            name='short_url',
            field=models.CharField(blank=True, max_length=20, unique=True),
        ),
    ]