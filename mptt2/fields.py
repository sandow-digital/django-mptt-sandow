"""
Model fields for working with trees.
"""

__all__ = ('TreeForeignKey', 'TreeOneToOneField', 'TreeManyToManyField')

from django.db import models
from mptt2.forms import TreeNodeChoiceField, TreeNodeMultipleChoiceField


class TreeForeignKey(models.ForeignKey):
    """
    Extends the foreign key, but uses mptt's ``TreeNodeChoiceField`` as
    the default form field.

    This is useful if you are creating models that need automatically
    generated ModelForms to use the correct widgets.
    """

    def formfield(self, **kwargs):
        """
        Use MPTT's ``TreeNodeChoiceField``
        """
        kwargs.setdefault('form_class', TreeNodeChoiceField)
        return super(TreeForeignKey, self).formfield(**kwargs)


class TreeOneToOneField(models.OneToOneField):
    def formfield(self, **kwargs):
        kwargs.setdefault('form_class', TreeNodeChoiceField)
        return super(TreeOneToOneField, self).formfield(**kwargs)


class TreeManyToManyField(models.ManyToManyField):
    def formfield(self, **kwargs):
        kwargs.setdefault('form_class', TreeNodeMultipleChoiceField)
        return super(TreeManyToManyField, self).formfield(**kwargs)

# South integration
try:
    from south.modelsinspector import add_introspection_rules
    add_introspection_rules([], ["^mptt2\.fields\.TreeForeignKey"])
    add_introspection_rules([], ["^mptt2\.fields\.TreeOneToOneField"])
    add_introspection_rules([], ["^mptt2\.fields\.TreeManyToManyField"])
except ImportError:
    pass
