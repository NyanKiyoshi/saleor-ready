# Generated by Django 2.0.3 on 2018-05-15 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0063_required_attr_value_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='productattribute',
            name='is_filter',
            field=models.BooleanField(db_index=True, default=True),
        ),
    ]
