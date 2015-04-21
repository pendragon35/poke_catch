import django
from pcalc.models import Rates

django.setup()

print Rates.objects.all()