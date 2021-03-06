# Generated by Django 2.1.4 on 2019-01-11 22:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('activity_type', models.CharField(choices=[('MV', 'verplaatst'), ('AL', 'geweizigd'), ('AP', 'goedgekeurd')], default='AL', max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_admin', models.BooleanField(default=False)),
                ('user_name', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_id', models.CharField(max_length=50)),
                ('answered', models.BooleanField(default=False)),
                ('upload_date', models.DateTimeField()),
                ('title', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=200)),
                ('question_document', models.CharField(max_length=200)),
                ('answer', models.TextField(blank=True)),
                ('status', models.CharField(choices=[('TD', 'Nieuw'), ('IP', 'Mee Bezig'), ('NV', 'Afgerond'), ('AP', 'Goedgekeurd')], default='TD', max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Subquestion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('parent_question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='q_answering.Question')),
            ],
        ),
        migrations.CreateModel(
            name='Verification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('executing_employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='q_answering.Employee')),
                ('target_question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='q_answering.Question')),
            ],
        ),
        migrations.AddField(
            model_name='activity',
            name='executing_employee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='q_answering.Employee'),
        ),
        migrations.AddField(
            model_name='activity',
            name='target_question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='q_answering.Question'),
        ),
    ]
