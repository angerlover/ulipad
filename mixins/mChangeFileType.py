#   Programmer:     limodou
#   E-mail:         limodou@gmail.com
#  
#   Copyleft 2006 limodou
#  
#   Distributed under the terms of the GPL (GNU Public License)
#  
#   UliPad is free software; you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation; either version 2 of the License, or
#   (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with this program; if not, write to the Free Software
#   Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
#
#   $Id: mChangeFileType.py 1457 2006-08-23 02:12:12Z limodou $

__doc__ = 'Process changing file type event'

from modules import Mixin

def on_document_lang_enter(win, document):
    win.mainframe.changefiletype.enter(win.mainframe, document)
Mixin.setPlugin('editctrl', 'on_document_lang_enter', on_document_lang_enter)

def on_document_lang_leave(win, filename, languagename):
    win.mainframe.changefiletype.leave(win.mainframe, filename, languagename)
Mixin.setPlugin('editctrl', 'on_document_lang_leave', on_document_lang_leave)

def afterinit(win):
    import ChangeFileType

    win.changefiletype = ChangeFileType.ChangeFileType()
Mixin.setPlugin('mainframe', 'afterinit', afterinit)
