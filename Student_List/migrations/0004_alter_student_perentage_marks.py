# Generated by Django 5.1.1 on 2024-10-20 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Student_List', '0003_alter_student_student_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='perentage_marks',
            field=models.DecimalField(decimal_places=2, max_digits=4),
        ),
    ]