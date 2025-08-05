from sqeleton.databases import sap_iq as iq
from .base import ReladiffDialect


class SapIQDialect(iq.SapIQDialect, iq.Mixin_MD5, iq.Mixin_NormalizeValue, ReladiffDialect):
    pass


class SapIQ(iq.SapIQ):
    dialect = SapIQDialect()
