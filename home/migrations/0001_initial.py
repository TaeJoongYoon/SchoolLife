# Generated by Django 2.0 on 2018-06-13 07:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('category', models.CharField(max_length=12, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('dept_name', models.CharField(max_length=10, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='FreeComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='FreePost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=25)),
                ('photo', models.ImageField(upload_to='')),
                ('content', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Instructor',
            fields=[
                ('name', models.CharField(max_length=4, primary_key=True, serialize=False)),
                ('dept_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Department')),
            ],
        ),
        migrations.CreateModel(
            name='LectureComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='LecturePost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=25)),
                ('content', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='MarketComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='MarketPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=25)),
                ('photo', models.ImageField(upload_to='')),
                ('content', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.CharField(max_length=8, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=8)),
                ('name', models.CharField(max_length=4)),
                ('nickname', models.CharField(max_length=10)),
                ('dept_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Department')),
            ],
        ),
        migrations.AddField(
            model_name='marketpost',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Student'),
        ),
        migrations.AddField(
            model_name='marketcomment',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Student'),
        ),
        migrations.AddField(
            model_name='marketcomment',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.MarketPost'),
        ),
        migrations.AddField(
            model_name='lecturepost',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Student'),
        ),
        migrations.AddField(
            model_name='lecturepost',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Course'),
        ),
        migrations.AddField(
            model_name='lecturecomment',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Student'),
        ),
        migrations.AddField(
            model_name='lecturecomment',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.LecturePost'),
        ),
        migrations.AddField(
            model_name='freepost',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Student'),
        ),
        migrations.AddField(
            model_name='freecomment',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Student'),
        ),
        migrations.AddField(
            model_name='freecomment',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.FreePost'),
        ),
        migrations.AddField(
            model_name='course',
            name='name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Instructor'),
        ),
    ]
