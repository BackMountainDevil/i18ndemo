#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
import fun
from model import nice
import locale
import gettext
from gettext import gettext as _


loc = locale.getlocale()
if not loc[0]  =="en_US":
  gettext.bindtextdomain(loc[0], localedir='locale')
  gettext.textdomain(loc[0])

fun.fun()
nice.nice()
print(_("Edit"))
print(_("Cancel"))
print(_("Confirm"))
