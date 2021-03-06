# Generated by Django 3.0.4 on 2020-03-04 15:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.PositiveIntegerField(unique=True)),
                ('name', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=256)),
                ('blue_one', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='blue_one', to='season2020.Team')),
                ('blue_three', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='blue_three', to='season2020.Team')),
                ('blue_two', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='blue_two', to='season2020.Team')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='season2020.Event')),
                ('red_one', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='red_one', to='season2020.Team')),
                ('red_three', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='red_three', to='season2020.Team')),
                ('red_two', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='red_two', to='season2020.Team')),
            ],
            options={
                'verbose_name_plural': 'matches',
            },
        ),
        migrations.AddField(
            model_name='event',
            name='teams',
            field=models.ManyToManyField(to='season2020.Team'),
        ),
    ]
