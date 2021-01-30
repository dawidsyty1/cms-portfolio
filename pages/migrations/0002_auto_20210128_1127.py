# Generated by Django 3.1.5 on 2021-01-28 11:27

from django.db import migrations, models
import django.db.models.deletion
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Seo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=255)),
                ('seo', wagtail.core.fields.StreamField([('tag', wagtail.core.blocks.RawHTMLBlock())], blank=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='portfoliopage',
            name='item',
        ),
        migrations.AddField(
            model_name='portfoliopage',
            name='items',
            field=wagtail.core.fields.StreamField([('title', wagtail.core.blocks.CharBlock()), ('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('body', wagtail.core.blocks.RichTextBlock(required=False))], blank=True),
        ),
        migrations.AlterField(
            model_name='portfoliopage',
            name='seo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='pages.seo'),
        ),
    ]