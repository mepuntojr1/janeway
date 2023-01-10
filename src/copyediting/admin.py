__copyright__ = "Copyright 2017 Birkbeck, University of London"
__author__ = "Martin Paul Eve & Andy Byers"
__license__ = "AGPL v3"
__maintainer__ = "Birkbeck Centre for Technology and Publishing"


from django.contrib import admin
from utils import admin_utils
from copyediting import models


class CopyeditAdmin(admin.ModelAdmin):
    list_display = ('pk', 'article', 'copyeditor', 'editor', 'assigned',
                    'decision', 'due')
    list_filter = ('assigned', 'due', 'date_decided',
                   'copyedit_reopened', 'decision')
    search_fields = ('article__title', 'copyeditor__first_name',
                     'copyeditor__last_name', 'copyeditor__email',
                     'editor__first_name', 'editor__last_name',
                     'editor__email', 'editor_note', 'copyeditor_note')
    raw_id_fields = ('article', 'copyeditor', 'editor')
    filter_horizontal = ('files_for_copyediting', 'copyeditor_files')
    date_hierarchy = ('assigned')

    inlines = [
        admin_utils.AuthorReviewInline
    ]


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('pk', 'author', 'assigned', 'notified', 'decision',
                    'date_decided', 'assignment')
    list_filter = ('assigned', 'notified', 'decision',
                   'date_decided')
    search_fields = ('assignment__article__title', 'author__first_name',
                     'author__last_name', 'author__email',
                     'assignment__editor_note', 'assignment__copyeditor_note')
    raw_id_fields = ('author', 'assignment')
    filter_horizontal = ('files_updated',)
    date_hierarchy = ('assigned')
    exclude = ('files_updated',)


admin_list = [
    (models.CopyeditAssignment, CopyeditAdmin),
    (models.AuthorReview, AuthorAdmin),
]

[admin.site.register(*t) for t in admin_list]
