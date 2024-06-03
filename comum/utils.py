from django.core.exceptions import ValidationError


def validate_file_size(value):
    filesize = value.size

    if filesize > 10485760:
        raise ValidationError("O arquivo excedeu o tamanho máximo permitido (10MB)")
    else:
        return value
