# Generated by Django 3.0.7 on 2020-06-20 09:18

from django.db import migrations, models
import django.db.models.deletion
import multiselectfield.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('user_id', models.CharField(max_length=100, unique=True)),
                ('user_type', models.CharField(choices=[('P', 'Patient'), ('H', 'Hospital')], default='Patient', max_length=2)),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='date-joined')),
                ('last_login', models.DateTimeField(auto_now=True, verbose_name='last-login')),
                ('is_admin', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Token',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department', models.CharField(max_length=3)),
                ('count', models.IntegerField(default=0)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.User')),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('age', models.IntegerField(default=None)),
                ('gender', models.CharField(choices=[('Male', 'M'), ('Female', 'F'), ('Others', 'O')], default='Male', max_length=6)),
                ('contact_no', models.IntegerField(unique=True)),
                ('social_status', models.CharField(choices=[('SC', 'SC'), ('General', 'Gen'), ('ST', 'ST'), ('OBC', 'OBC')], default='Gen', max_length=8)),
                ('prefd_hospital', models.CharField(max_length=100)),
                ('tokenNo', models.IntegerField(blank=True, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='accounts.User')),
            ],
        ),
        migrations.CreateModel(
            name='Hospital',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('address', models.CharField(max_length=250)),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('bed_capacity', models.CharField(max_length=250)),
                ('currently_free', models.CharField(max_length=250)),
                ('hasTokenSystem', models.BooleanField(default=False)),
                ('linkToTokenWebsite', models.URLField(blank=True, null=True)),
                ('specialities', multiselectfield.db.fields.MultiSelectField(choices=[('Allergy & Clinical Immunology', 'Allergy & Clinical Immunology'), ('Anaesthesia', 'Anaesthesia'), ('Bariatric & Metabolic Surgery', 'Bariatric & Metabolic Surgery'), ('Blood Disorders', 'Blood Disorders'), ('Breast Surgery', 'Breast Surgery'), ('Cardiac Anaesthesia', 'Cardiac Anaesthesia'), ('Cardiac Surgery', 'Cardiac Surgery'), ('Cardiology', 'Cardiology'), ('Cardiology - Interventional', 'Cardiology - Interventional'), ('Dental Sciences', 'Dental Sciences'), ('Dermatology', 'Dermatology'), ('Diabetes And Endocrinology', 'Diabetes And Endocrinology'), ('Dietetics & Clinical Nutrition', 'Dietetics & Clinical Nutrition'), ('ENT', 'ENT'), ('Geriatric Medicine', 'Geriatric Medicine'), ('Ophthalmology', 'Ophthalmology'), ('Foetal Medicine', 'Foetal Medicine'), ('Gastroenterology', 'Gastroenterology'), ('General Surgery', 'General Surgery'), ('General and Laparoscopic Surgery', 'General and Laparoscopic Surgery'), ('Gynaecology Oncology', 'Gynaecology Oncology'), ('Infectious Diseases', 'Infectious Diseases'), ('Infertility Medicine', 'Infertility Medicine'), ('Intensive Care', 'Intensive Care'), ('Internal Medicine', 'Internal Medicine'), ('Interventional Radiology', 'Interventional Radiology'), ('Laparoscopic, Gastro Intestinal, Bariatric & Metabolic Surgery', 'Laparoscopic, Gastro Intestinal, Bariatric & Metabolic Surgery'), ('Liver Transplant / Hepatobiliary Surgery', 'Liver Transplant / Hepatobiliary Surgery'), ('Medical Oncology', 'Medical Oncology'), ('Medical Oncology, Hematology And BMT', 'Medical Oncology, Hematology And BMT'), ('Mental Health and Behavioural Sciences', 'Mental Health and Behavioural Sciences'), ('Neonatology', 'Neonatology'), ('Nephrology', 'Nephrology'), ('Neuro & Spine Surgery', 'Neuro & Spine Surgery'), ('Neuro Radiology', 'Neuro Radiology'), ('Neurology', 'Neurology'), ('Non Invasive Cardiology', 'Non Invasive Cardiology'), ('Obstetrics and Gynaecology', 'Obstetrics and Gynaecology'), ('Onco Sciences', 'Onco Sciences'), ('Oral / Maxillofacial Surgery', 'Oral / Maxillofacial Surgery'), ('Orthopaedics & Spine Surgery', 'Orthopaedics & Spine Surgery'), ('Orthopaedics  Bone & Joint Surgery', 'Orthopaedics  Bone & Joint Surgery'), ('Orthopaedics  Hand & Upper Limb Surgery', 'Orthopaedics  Hand & Upper Limb Surgery'), ('Paediatric Cardiology', 'Paediatric Cardiology'), ('Paediatric Endocrinology', 'Paediatric Endocrinology'), ('Paediatric Nephrology', 'Paediatric Nephrology'), ('Paediatric Neurology', 'Paediatric Neurology'), ('Paediatric Oncology', 'Paediatric Oncology'), ('Paediatric Orthopaedics', 'Paediatric Orthopaedics'), ('Paediatric Pulmonology', 'Paediatric Pulmonology'), ('Paediatric Surgery', 'Paediatric Surgery'), ('Paediatrics', 'Paediatrics'), ('Pain management', 'Pain management'), ('Physiotherapy and Rehabilitation', 'Physiotherapy and Rehabilitation'), ('Plastic, Cosmetic & Reconstructive Surgery', 'Plastic, Cosmetic & Reconstructive Surgery'), ('DiabeticFoot Care', 'Diabetic Foot Care'), ('Pulmonology', 'Pulmonology'), ('Radiation Oncology', 'Radiation Oncology'), ('Radiology', 'Radiology'), ('Rheumatology', 'Rheumatology'), ('Arthroscopic Surgery', 'Arthroscopic Surgery'), ('Surgical Oncology', 'Surgical Oncology'), ('Trauma & Emergency Medicine', 'Trauma & Emergency Medicine'), ('Urology & Andrology', 'Urology & Andrology'), ('Urology, Andrology & Transplant Surgery', 'Urology, Andrology & Transplant Surgery'), ('Vascular Surgery', 'Vascular Surgery')], default=None, max_length=1464)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='accounts.User')),
            ],
        ),
    ]
