from django.db.models import TextChoices
from django.utils.translation import gettext_lazy as _


class TiposAgendamento(TextChoices):
    TESTDRIVE = 'TestDrive', _('Test-drive')
    TROCAOLEO = 'TrocaOleo', _('Troca de Óleo')
