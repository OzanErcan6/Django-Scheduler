from __future__ import unicode_literals

from builtins import format

from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db import models
from django.core.urlresolvers import reverse
from django.utils.text import Truncator


class Board(models.Model):
    name = models.CharField(max_length=30, unique=True)

    class Meta:
        verbose_name = u'Rooms'
        verbose_name_plural = u'Rooms'

    def __str__(self):
        return self.name

    def get_posts_count(self):
        return Post.objects.filter(topic__board=self).count()

    def get_last_post(self):
        return Post.objects.filter(topic__board=self).order_by('-created_at').first()


class Topic(models.Model):
    subject = models.CharField(max_length=160, help_text='Max 160 char.')
    board = models.ForeignKey(Board, related_name='topics')
    starter = models.ForeignKey(User, related_name='topics')
    day = models.DateField(u'Day of the event', help_text=u'eg. YYYY-MM-DD ', blank=False)
    start_time = models.TimeField()
    end_time = models.TimeField()
    room = models.CharField(max_length=30)

    class Meta:
        verbose_name = u'Reservations'
        verbose_name_plural = u'Reservations'

    def check_overlap(self, fixed_start, fixed_end, new_start, new_end):
        overlap = False
        if new_start == fixed_end or new_end == fixed_start:  # edge case
            overlap = False
        elif (fixed_start <= new_start <= fixed_end) or (
                fixed_start <= new_end <= fixed_end):  # innner limits
            overlap = True
        elif new_start <= fixed_start and new_end >= fixed_end:  # outter limits
            overlap = True

        return overlap

    def get_absolute_url(self):
        url = reverse('admin:%s_%s_change' % (self._meta.app_label, self._meta.model_name), args=[self.id])
        return u'<a href="%s">%s</a>' % (url, str(self.start_time))

    def clean(self):
        if self.end_time <= self.start_time:
            raise ValidationError('Ending times must after starting times')

        events = Topic.objects.filter(day=self.day, room=self.room)
        if events.exists():
            for event in events:
                if self.check_overlap(event.start_time, event.end_time, self.start_time, self.end_time):
                    raise ValidationError(
                        'There is an overlap with another event: ' + str(event.day) + ', ' + str(
                            event.start_time) + '-' + str(event.end_time))

    def __str__(self):
        return self.subject


class Post(models.Model):
    message = models.TextField(max_length=4000)
    topic = models.ForeignKey(Topic, related_name='posts')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True)
    created_by = models.ForeignKey(User, related_name='posts')
    updated_by = models.ForeignKey(User, null=True, related_name='+')

    def __str__(self):
        truncated_message = Truncator(self.message)
        return truncated_message.chars(30)
