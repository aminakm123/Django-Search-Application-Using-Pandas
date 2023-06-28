import os
import pandas as pd
from django.shortcuts import render
from django.db.models.signals import post_migrate
from django.dispatch import receiver
from .models import Dish


# Define a signal receiver to load data after migrations
@receiver(post_migrate)
def load_data(sender, **kwargs):
    if sender.name == 'dish_search_app':
        data_path = os.path.join(os.path.dirname(__file__), 'data', 'restaurants_small.csv')
        df = pd.read_csv(data_path)

        for _, row in df.iterrows():
            Dish.objects.get_or_create(
                id=row['id'],
                name=row['name'],
                location=row['location'],
                items=row['items']
            )

# we can use this code in command prompt instead of the above load_data view, python manage.py shell -c "from dish_search_app.models import Dish; Dish.load_data_from_csv()"

# Define the search view function
def search_dishes(request):
    query = request.GET.get('query', '')
    dishes = Dish.objects.filter(items__icontains=query)

    return render(request, 'search.html', {'query': query, 'dishes': dishes})