from sqeleton.databases import impala as imp
from .base import ReladiffDialect


class ImpalaDialect(imp.ImpalaDialect, imp.Mixin_MD5, imp.Mixin_NormalizeValue, ReladiffDialect):
    pass


class Impala(imp.Impala):
    dialect = ImpalaDialect()
