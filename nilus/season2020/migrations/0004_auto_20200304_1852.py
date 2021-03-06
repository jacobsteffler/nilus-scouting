# Generated by Django 3.0.4 on 2020-03-05 00:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('season2020', '0003_remove_scoutresponse_event'),
    ]

    operations = [
        migrations.AddField(
            model_name='scoutresponse',
            name='auto_can_intake',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='scoutresponse',
            name='auto_high_balls',
            field=models.PositiveIntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='scoutresponse',
            name='auto_low_balls',
            field=models.PositiveIntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='scoutresponse',
            name='tele_control_panel',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='scoutresponse',
            name='tele_did_climb',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='scoutresponse',
            name='tele_farthest_shot',
            field=models.CharField(blank=True, choices=[('FT', 'Far trench'), ('NT', 'Near trench'), ('IL', 'Initiation line'), ('UC', 'Up close')], max_length=2, null=True),
        ),
        migrations.AddField(
            model_name='scoutresponse',
            name='tele_high_balls',
            field=models.PositiveIntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='scoutresponse',
            name='tele_low_balls',
            field=models.PositiveIntegerField(blank=True, default=0, null=True),
        ),
    ]
