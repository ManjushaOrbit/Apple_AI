# Generated by Django 5.0.6 on 2024-06-14 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CandidateData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('post_applied', models.CharField(max_length=100)),
                ('total_month_experinec', models.CharField(blank=True, max_length=200, null=True)),
                ('total_year_experinec', models.PositiveIntegerField(null=True)),
                ('current_ctc', models.PositiveIntegerField(null=True)),
                ('expected_ctc', models.PositiveIntegerField(null=True)),
                ('experinece_in_sales_and_services', models.TextField(null=True)),
                ('notice_period', models.CharField(choices=[('1M', '1 month'), ('2M', '2 months'), ('3M', '3 months')], default='0M', max_length=10)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], default='M', max_length=1)),
                ('reason_for_this_job', models.TextField(null=True)),
                ('resumefile', models.FileField(upload_to='resumes/')),
                ('reffered_by', models.CharField(max_length=500, null=True)),
            ],
        ),
    ]
