from django.urls import reverse

from .historized.base import BaseHistorical as BaseHistoricalP


class AdminViewMixin:
    @classmethod
    def get_viewname(cls, view):
        module = cls._meta.app_label
        model_name = cls._meta.model_name
        return f'admin:{module}_{model_name}_{view}'

    @property
    def admin_url(self):
        return reverse(self.get_viewname('change'), args=[self.suid])


class BaseHistorical(AdminViewMixin, BaseHistoricalP):
    class Meta:
        abstract = True
