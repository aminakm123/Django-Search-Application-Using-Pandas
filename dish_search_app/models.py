import os
import pandas as pd
from django.db import models

class Dish(models.Model):
    id = models.CharField(primary_key=True,max_length=255)
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    items = models.TextField()

    def __str__(self):
        return self.name

    @staticmethod
    def load_data_from_csv():
        data_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'restaurants_small.csv')
        df = pd.read_csv(data_path)
        dishes = []

        for _, row in df.iterrows():
            dish = Dish(name=row['name'], location=row['location'], dishes=row['dishes'])
            dishes.append(dish)

        Dish.objects.bulk_create(dishes)

