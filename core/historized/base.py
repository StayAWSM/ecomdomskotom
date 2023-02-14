from .uided import PUided
from .dated import Dated
from .versioned import Versioned
from .historized import Historized


class BaseHistorical(PUided, Dated, Versioned, Historized):  # type: ignore
    class Meta:
        ordering = ['created']
        abstract = True
