import csv  # https://docs.python.org/3/library/csv.html

# https://django-extensions.readthedocs.io/en/latest/runscript.html

# python3 manage.py runscript many_load

from recipe.models import Recipe, Ingredient, OwnIngredient, Nutrition, Time

def run():
    fhand = open('smaller_data.csv')
    reader = csv.reader(fhand)
    next(reader) # Advance past the header

    Recipe.objects.all().delete()
    Ingredient.objects.all().delete()
    OwnIngredient.objects.all().delete()
    Nutrition.objects.all().delete()
    Time.objects.all().delete()

    # Format
    # email,role,course
    # jane@tsugi.org,I,Python
    # ed@tsugi.org,L,Python

    for row in reader:
        print(row)

        r = Recipe(name=row[1], minutes=row[2], n_steps=row[4], steps=row[5], ingredients=row[6], n_ingredients=row[7])
        r.save()
        # p, created = Person.objects.get_or_create(email=row[0])
        # c, created = Course.objects.get_or_create(title=row[2])

        # r = Membership.LEARNER
        # if row[1] == 'I' : r = Membership.INSTRUCTOR
        # m = Membership(role=r,person=p, course=c)
        # m.save()