from django.core.validators import RegexValidator, ValidationError
from django.utils.translation import ugettext_lazy as _


class DefaultValidator(object):
    char_only = RegexValidator(r'^[a-zA-Z-\s]*$', 'Only alphabetic characters are allowed.')


def validate_phonenumber(value):
    no = list(value)
    country_code = no[:4]
    if not country_code[0] == '+':
        raise ValidationError(
            _('%(value)s is not a valid Phone Number, it must begin with a country code"'),
            params={'value': value}
        )
    body = no[4:]
    if len(body) != 9:
        raise ValidationError(
            _('%(value)s is not a valid Phone Number!!'),
            params={'value': value}
        )

_validator = DefaultValidator
validators_list = [_validator.char_only, ]

