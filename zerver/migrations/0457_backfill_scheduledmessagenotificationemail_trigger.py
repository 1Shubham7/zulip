# Generated by Django 4.2.1 on 2023-06-20 12:07

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("zerver", "0456_alter_usergroup_can_mention_group"),
    ]

    operations = [
        migrations.RunSQL(
            """
            UPDATE zerver_scheduledmessagenotificationemail
            SET trigger = 'stream_wildcard_mentioned'
            WHERE trigger = 'wildcard_mentioned';
            """,
            reverse_sql="""
            UPDATE zerver_scheduledmessagenotificationemail
            SET trigger = 'wildcard_mentioned'
            WHERE trigger = 'stream_wildcard_mentioned';
            """,
        ),
        migrations.RunSQL(
            """
            UPDATE zerver_scheduledmessagenotificationemail
            SET trigger = 'stream_wildcard_mentioned_in_followed_topic'
            WHERE trigger = 'followed_topic_wildcard_mentioned';
            """,
            reverse_sql="""
            UPDATE zerver_scheduledmessagenotificationemail
            SET trigger = 'followed_topic_wildcard_mentioned'
            WHERE trigger = 'stream_wildcard_mentioned_in_followed_topic';
            """,
        ),
    ]
