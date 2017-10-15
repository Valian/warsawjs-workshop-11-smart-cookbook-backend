from rest_framework import serializers

from smart_cookbook import models


class IngredientQuantitySerializer(serializers.ModelSerializer):

    class Meta:
        model = models.IngredientQuantity
        fields = "__all__"


class IngredientSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Ingredient
        fields = "__all__"


class SimpleRecipeSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Recipe
        fields = "__all__"


class RecipeSerializer(SimpleRecipeSerializer):
    ingredients = IngredientQuantitySerializer(many=True)
