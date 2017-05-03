# -*- coding: utf-8 -*-
# Copyright (c) 2011 by Pablo Martín <goinnn@gmail.com>
#
# This software is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This software is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with this software.  If not, see <http://www.gnu.org/licenses/>.
import sys

from django.conf import settings
from django.forms import widgets
from django.forms.utils import flatatt
from django.template.loader import render_to_string
from django.utils.safestring import mark_safe

try:
    from django.utils.simplejson import JSONEncoder
except ImportError:
    from json import JSONEncoder


def get_tinyMCE_js():
    return getattr(settings,
                   'INPLACE_TINYMCE_JS',
                   '//tinymce.cachefly.net/4.2/tinymce.min.js')


class TinyMCE(widgets.Textarea):
    """
    TinyMCE widget.

    You can customize the mce_settings by overwriting instance mce_settings,
    or add extra options using update_settings
    """

    mce_settings = dict(relative_urls=False,
                        theme="modern",
                        inline=True,
                        layout="stack",
                        fixed_toolbar_container=True,
                        strict_loading_mode=1,
                        plugins=("template advlist autolink lists link image charmap hr anchor "
                                 "searchreplace wordcount visualblocks visualchars code fullscreen "
                                 "insertdatetime media nonbreaking table contextmenu directionality"),
                        toolbar=("template insertfile undo redo | styleselect | bold italic | alignleft aligncenter alignright alignjustify | "
                                 "bullist numlist outdent indent | link image"),
                        mode="exact",
                        file_browser_callback='FileBrowser',
                        content_css='/static/admin_css/editor.css?v=4',
                        style_formats = [
                            {'title': 'Header 1', 'block': 'h1'},
                            {'title': 'Header 2', 'block': 'h2'},
                            {'title': 'Header 3', 'block': 'h3'},
                            {'title': 'Header 4', 'block': 'h4'},
                            {'title': 'Header 5', 'block': 'h5'},
                            {'title': 'Header 6', 'block': 'h6'},
                            {'title': 'Div', 'block': 'div'},
                            {'title': 'Paragraph', 'block': 'p'},
                            {'title': 'Alpha List', 'selector': 'ol', 'styles': {'list-style-type': 'lower-alpha'}},
                            {'title': 'Button', 'selector': 'a', 'classes': 'btn'},
                        ],
                        templates = [
                            {'title': '1 Column', 'description': '1 Full Width Column.',
                                'url': '/static/tinymce_templates/one_col.html'},
                            {'title': '2 Column', 'description': '2 Equal Columns',
                                'url': '/static/tinymce_templates/2-col.html'},
                            {'title': '3 Column', 'description': '3 Equal Columns',
                                'url': '/static/tinymce_templates/3-col.html'},
                            {'title': '4 Column', 'description': '4 Equal Columns',
                                'url': '/static/tinymce_templates/4-col.html'},
                            {'title': '2 Column Wide Right', 'description': 'One Skinny Column & One Wide Column',
                                'url': '/static/tinymce_templates/wide_col_right.html'},
                            {'title': '2 Column Wide Left', 'description': 'One Skinny Column & One Wide Column',
                                'url': '/static/tinymce_templates/wide_col_left.html'},
                        ],)

    class Media:
        js = (get_tinyMCE_js(),)

    def __init__(self, extra_mce_settings=None,
                 config=None, width=None, *args, **kwargs):
        super(TinyMCE, self).__init__(*args, **kwargs)
        extra_mce_settings = extra_mce_settings or {}
        config = config or {}
        self.mce_settings = TinyMCE.mce_settings.copy()
        self.mce_settings['setup'] = ''.join(render_to_string(
            'inplaceeditform_extra_fields/adaptor_tiny/setup.js', config).splitlines())
        self.mce_settings['language'] = getattr(settings, 'TINYMCE_LANG', 'en')
        if width is not None and width < 700:
            toolbar_items = self.mce_settings['toolbar'].split(' | ')
            if width < 700 and width > 350:
                toolbar1 = ' | '.join(toolbar_items[:int(len(toolbar_items) / 2)])
                toolbar2 = ' | '.join(toolbar_items[int(len(toolbar_items) / 2):])
                self.mce_settings['toolbar1'] = toolbar1
                self.mce_settings['toolbar2'] = toolbar2
            if width < 350:
                toolbar1 = ' | '.join(toolbar_items[:int(len(toolbar_items) / 3)])
                toolbar2 = ' | '.join(toolbar_items[int(len(toolbar_items) / 3):int(2 * len(toolbar_items) / 3)])
                toolbar3 = ' | '.join(toolbar_items[int(2 * len(toolbar_items) / 3):])
                self.mce_settings['toolbar1'] = toolbar1
                self.mce_settings['toolbar2'] = toolbar2
                self.mce_settings['toolbar3'] = toolbar3
            del self.mce_settings['toolbar']

        self.mce_settings.update(extra_mce_settings)
        self.mce_settings.update(config)

    def render(self, name, value, attrs=None):
        if value is None:
            value = ''
        if sys.version_info[0] == 2:
            from django.utils.encoding import smart_unicode
            value = smart_unicode(value)
        final_attrs = self.build_attrs(attrs, name=name)
        self.mce_settings['elements'] = "id_%s" % name
        mce_json = JSONEncoder().encode(self.mce_settings).replace("\"function", "function").replace("}\"", "}")
        safe_value = mark_safe(u'''<div%s>%s</div>
                <script type="text/javascript">

                    var tmce_id;
                    var tmce_value;
                    var tmce_type;
                    var tmce_win;
                    var tmfb_win;

                    function FileBrowser(id, value, type, win) {
                        // Do custom browser logic
                        // var url = '/site_media/images/tnwa_logo.png';
                        // var fieldElm = win.document.getElementById(id);
                        // fieldElm.value = url;
                        var cmsURL = '/admin/filebrowser/browse/?pop=2';
                        cmsURL = cmsURL + '&type=' + type;

                        tmce_id = id;
                        tmce_value = value;
                        tmce_type = type;
                        tmce_win = win;

                        tmfb_win = tinymce.activeEditor.windowManager.open({
                            url: cmsURL,
                            title: 'Choose or Upload a File',
                            resizable: true,
                            scrollbars: true,
                            maximizable: true,
                            width: 940,
                            height: 600
                            },{
                            window: win,
                            input: value,
                            editor_id: id
                        });
                        return false;
                    }

                    tinyMCE.init(%s);
                    setTimeout(function () {
                        $("#%s").focus();
                    }, 500);
                </script>''' % (flatatt(final_attrs),
                                value,
                                mce_json,
                                self.mce_settings['elements']))
        return safe_value.replace('"FileBrowser"', "FileBrowser")
