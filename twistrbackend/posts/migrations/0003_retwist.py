# Generated by Django 2.2.6 on 2019-11-27 05:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('posts', '0002_post_author'),
    ]

    operations = [
        migrations.CreateModel(
            name='Retwist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text_body', models.CharField(max_length=280)),
                ('like_count', models.IntegerField(default=0)),
                ('posted_date', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('original_post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='retwist_original_post', to='posts.Post')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='retwist_post', to='posts.Post')),
            ],
        ),
    ]
