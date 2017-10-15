from django.db import models


class Ingredient(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    picture = models.ImageField(upload_to='ingredients', null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"#{self.pk} {self.name} price {self.price}"


class Recipe(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    picture = models.ImageField(upload_to='ingredients', null=True, blank=True)
    cooking_steps = models.TextField()
    preparation_time = models.DurationField()
    type = models.CharField(max_length=100)

    def __str__(self):
        return f"#{self.pk} {self.name} type {self.type}"


class IngredientQuantity(models.Model):
    ingredient = models.ForeignKey(Ingredient, related_name='ingredients_quantities')
    recipe = models.ForeignKey(Recipe, related_name='ingredients_quantities')
    quantity = models.SmallIntegerField(default=1)
