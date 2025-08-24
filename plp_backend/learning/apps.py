from django.apps import AppConfig

class LearningConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'learning'
    verbose_name = "AI-Powered Learning"

    # Optional: signals ready
    def ready(self):
        import learning.signals  # if you plan to use signals
