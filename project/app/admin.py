import json
from datetime import datetime

from django.contrib import admin
from django.http import HttpResponse

from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('post_id', 'post_title', 'formatted_date_create')
    search_fields = ('post_title', 'post_text')
    actions = ['export_selected_news_to_json']

    def has_add_permission(self, request):
        """Убирает возможность добавлять новости."""
        return False

    def formatted_date_create(self, obj):
        """Отображения отформатированного времени публицкации новости."""
        timestamp = int(obj.date_create)
        date = datetime.fromtimestamp(timestamp)
        return date.strftime("%Y-%m-%d %H:%M:%S")
    formatted_date_create.short_description = 'Дата создания'

    def export_selected_news_to_json(self, request, queryset):
        """Выгрузка выбранных новостей в json файл."""
        selected_news = queryset.values(
            'post_id',
            'post_title',
            'date_create',
            'post_text'
        )
        json_data = json.dumps(
            list(selected_news),
            indent=4,
            ensure_ascii=False
        )
        response = HttpResponse(json_data, content_type='application/json')
        response['Content-Disposition'] = (
            'attachment; filename="selected_news.json"'
        )
        return response

    export_selected_news_to_json.short_description = (
        'Экспортировать выбранные новости в JSON'
    )
