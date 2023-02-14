from .uided import PUided
from .dated import Dated
from .versioned import Versioned
from .historized import Historized


class BasePHistorical(PUided, Dated, Versioned, Historized):  # type: ignore
    class Meta:
        ordering = ['created']
        abstract = True
