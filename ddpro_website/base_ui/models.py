from django.db import models
from django.utils.translation import ugettext_lazy as _


class About(models.Model):
    """
    Homepage about texts
    """
    heading = models.CharField(verbose_name=_('Heading'), max_length=255, default="")
    text_html = models.TextField(verbose_name=_('Text'), default="")

    def __str__(self):
        return self.heading

    class Meta:
        verbose_name = _('About')
        verbose_name_plural = _('About')
        db_table = 'base_ui_about'


class TeamMember(models.Model):
    """
    Homepage roles
    """
    first_name = models.CharField(verbose_name=_('First name'), max_length=255, default="")
    last_name = models.CharField(verbose_name=_('Last name'), max_length=255, default="")
    image = models.FileField(verbose_name=_('Image'), upload_to='features_image', blank=True, null=True)
    priority = models.IntegerField(verbose_name=_('Priority'), default=0)
    roles = models.TextField(verbose_name=_('Roles'), default="")

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)

    class Meta:
        verbose_name = _('Team')
        verbose_name_plural = _('Teams')
        db_table = 'base_ui_team'


class Product(models.Model):
    """
    Items from product list on main page
    """
    title = models.CharField(verbose_name=_('Title'), max_length=255, default="")
    image = models.FileField(verbose_name=_('Image'), upload_to='features_image', blank=True, null=True)
    short_description = models.TextField(verbose_name=_('Short description'), default="")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Product')
        verbose_name_plural = _('Products')
        db_table = 'base_ui_product'