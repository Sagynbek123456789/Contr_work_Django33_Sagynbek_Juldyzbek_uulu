from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def validate_summary_not_empty(value):
    if not value:
        raise ValidationError(
            _('description не может быть пустым.')
        )


def validate_description_length(value):
    if len(value) < 10:
        raise ValidationError(
            _('Длина описания должна быть не менее 10 символов.')
        )
