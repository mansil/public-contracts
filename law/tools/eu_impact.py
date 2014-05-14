## setup the Django with public settings for using the database.
if __name__ == "__main__":
    from . import set_up
    set_up.set_up_django_environment('law.tools.settings_public')

from law.models import Document


if __name__ == "__main__":
    # prints the relative number of laws that have no text
    import datetime
    date = datetime.date(1966, 1, 1)

    documents = Document.objects.filter(date__gt=date)\
        .exclude(type_id__in=[95, 97, 145, 150])

    total = documents.count()
    actual = documents.filter(text=None).count()

    print(actual*1./total*100)
