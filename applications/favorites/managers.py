from django.db import models

# PROCEDURE FOR ENTRY

class FavoritesManager(models.Manager):
    
    def entries_user(self, usuario):
        return self.filter(
            entry__public=True,
            user=usuario
        ).order_by('-created')