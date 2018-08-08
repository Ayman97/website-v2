from django.db import models as django_models
from . import models as library_models

from decimal import Decimal
from model_utils.managers import InheritanceManager

from caching.base import CachingManager


class WorkshopManagerCacheable(CachingManager):
    def get_workshop(self):
        return library_models.Workshop.objects


class WorkshopManager(django_models.Manager):
    workshop_manager = WorkshopManagerCacheable()

    def with_shown_percentage(self, user):
        workshops = self.workshop_manager.get_workshop()
        workshops = workshops.annotate(

            shown_count=django_models.Count('modules__lessons', filter=django_models.Q(
                modules__lessons__id__in=user.lessons.values('id'))),

            total_count=django_models.Count('modules__lessons'))

        # print('fields = ', result[0].shown_count, result[0].total_count)

        workshops = workshops.annotate(
            shown_percentage=django_models.ExpressionWrapper(
                (float(100.0) * django_models.F('shown_count') /
                 django_models.F('total_count')),
                output_field=django_models.DecimalField(max_digits=2, decimal_places=2)))

        #print('calculated = ', result[0].shown_count / result[0].total_count)
        #print('queried = ', result[0].shown_percentage)

        return workshops


class BaseLessonManager(InheritanceManager, CachingManager):
    def with_is_shown(self, user):

        user_shown_lessons = user.lessons.values('id')

        shown_user_case = django_models.Case(
            django_models.When(id__in=user_shown_lessons,
                               then=django_models.Value(True)),
            default=django_models.Value(False),
            output_field=django_models.BooleanField())

        return self.get_queryset().annotate(
            is_shown=shown_user_case)
