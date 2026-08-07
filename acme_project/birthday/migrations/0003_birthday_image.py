from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('birthday', '0002_birthday_unique_constraint'),
    ]

    operations = [
        migrations.AddField(
            model_name='birthday',
            name='image',
            field=models.ImageField(
                blank=True,
                upload_to='birthdays_images/',
                verbose_name='Фото',
            ),
        ),
    ]
