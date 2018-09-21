#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import absolute_import

from django import template
from django.utils.html import format_html

from . import OCTICON_DATA

register = template.Library()


class Octicon(object):
    def __init__(self, symbol, **options):
        self.symbol = symbol
        self.octicon = OCTICON_DATA.get(self.symbol)
        if not self.octicon:
            raise ValueError(
                "Couldn't find octicon symbol for {}".format(self.symbol)
            )

        self.path = self.octicon['path']
        self.width = int(self.octicon['width'])
        self.height = int(self.octicon['height'])

        self.keywords = self.octicon['keywords']

        self.options = options
        self.options.update({
            "class": self.classes,
            "viewBox": self.viewBox,
            "version": "1.1"
        })

        self.options.update(self.size)

        self.options.update(self.a11y)

    @property
    def to_svg(self):
        return "<svg {}>{}</svg>".format(self.html_attributes, self.path)

    @property
    def html_attributes(self):
        attrs = ""
        for (attr, value) in self.options.items():
            attrs += '{}="{}" '.format(attr, value)
        return attrs.strip()

    @property
    def a11y(self):
        accessible = {}

        if not self.options.get('aria-label'):
            accessible['aria-hidden'] = 'true'
        else:
            accessible['role'] = 'img'

        return accessible

    @property
    def classes(self):
        classes = 'octicon octicon-{} '.format(self.symbol) + self.options.get('class', '')  # noqa
        return classes.strip()

    @property
    def viewBox(self):
        return "0 0 {} {}".format(self.width, self.height)

    @property
    def size(self):
        size = {
            'width': self.width,
            'height': self.height
        }

        # if a custom width or height is passed in
        if self.options.get('width') or self.options.get('height'):
            if self.options.get('width'):
                size['width'] = self.options.get('width')
            else:
                size['width'] = self._calculate_width(self.options['height'])

            if self.options.get('height'):
                size['height'] = self.options.get('height')
            else:
                size['height'] = self._calculate_height(self.options['width'])

        return size

    def _calculate_width(self, height):
        return int((int(height) * self.width) / self.height)

    def _calculate_height(self, width):
        return int((int(width) * self.height) / self.width)


@register.simple_tag
def octicon(symbol, **options):
    icon = Octicon(symbol, **options)
    return format_html(icon.to_svg)
