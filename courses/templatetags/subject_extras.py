from django import template

from courses.models import Subject

register = template.Library()


@register.inclusion_tag('subjects_nav.html')
def nav_subjects_list():
    subjects = Subject.objects.all()
    return {'subjects': subjects}
