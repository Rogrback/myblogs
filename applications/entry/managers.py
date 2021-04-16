from django.db import models

# PROCEDURE FOR ENTRY

class EntryManager(models.Manager):

    def entry_in_coverpage(self):
        return self.filter(
            public=True,
            cover_page=True,
        ).order_by('-created').first()

    # Return the last 4 entrys in home
    def entry_in_home(self):
        return self.filter(
            public=True,
            in_home=True,
        ).order_by('-created')[:4]

    # Return the last 6 entrys recents
    def entry_recents(self):
        return self.filter(
            public=True,
        ).order_by('-created')[:6]

    # Procedure for search entrys for category or key word
    def search_entry(self, kword, category):
        if len(category) > 0:
            return self.filter(
                category__short_name=category,
                title__icontains=kword,
                public=True
            ).order_by('-created')

        else:
            return self.filter(
                title__icontains=kword,
                public=True
            ).order_by('-created')
    