from datetime import datetime
from datetime import date


mi_fecha = datetime(1997, 3, 10)

tiempo = mi_fecha.today() - mi_fecha
print(date(tiempo))

