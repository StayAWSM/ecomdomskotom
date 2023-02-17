import datetime

from django.utils.translation import gettext_lazy as _

TABLE_NUMBERS = [
    (1, _('Стол №1')),
    (2, _('Стол №2')),
    (3, _('Стол №3')),
    (4, _('Стол №4')),
    (5, _('Стол №5')),
    (6, _('Стол №6')),
    (7, _('Стол №7')),
    (8, _('Стол №8')),
    (9, _('Стол №9')),
    (10, _('Стол №10')),
    (11, _('Стол №11')),
    (12, _('Стол №12')),
]

BOOKING_TIME_INTERVALS = [
    (datetime.time(11, 0), _('11:00')), (datetime.time(11, 30), _('11:30')),
    (datetime.time(12, 0), _('12:00')), (datetime.time(12, 30), _('12:30')),
    (datetime.time(13, 0), _('13:00')), (datetime.time(13, 30), _('13:30')),
    (datetime.time(14, 0), _('14:00')), (datetime.time(14, 30), _('14:30')),
    (datetime.time(15, 0), _('15:00')), (datetime.time(15, 30), _('15:30')),
    (datetime.time(16, 0), _('16:00')), (datetime.time(16, 30), _('16:30')),
    (datetime.time(17, 0), _('17:00')), (datetime.time(17, 30), _('17:30')),
    (datetime.time(18, 0), _('18:00')), (datetime.time(18, 30), _('18:30')),
    (datetime.time(19, 0), _('19:00')), (datetime.time(19, 30), _('19:30')),
    (datetime.time(20, 0), _('20:00')), (datetime.time(20, 30), _('20:30'))
]
