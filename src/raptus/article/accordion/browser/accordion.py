from zope import interface

from Products.CMFCore.utils import getToolByName

from raptus.article.listings.browser import listing

from raptus.article.core import RaptusArticleMessageFactory as _


class IAccordion(interface.Interface):
    """ Marker interface for the accordion viewlet
    """


class Component(listing.ComponentLeft):
    """ Component which lists the articles in an accordion
    """

    title = _(u'Accordion')
    description = _(u'List of the contained articles in an accordion.')
    image = '++resource++accordion.gif'
    interface = IAccordion
    viewlet = 'raptus.article.accordion'


class Viewlet(listing.ViewletLeft):
    """ Viewlet listing the articles in an accordion
    """
    type = "accordion"
    thumb_size = None
    component = "accordion"

    @property
    def cssClass(self):
        props = getToolByName(self.context, 'portal_properties').raptus_article
        return 'accordion-listing ' + (props.getProperty('accordion_onlyone', True) and 'onlyone' or 'multiple')
