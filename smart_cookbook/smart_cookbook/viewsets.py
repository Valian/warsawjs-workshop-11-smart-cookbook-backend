from rest_framework import viewsets

from smart_cookbook import models, serializers


class IngredientViewset(viewsets.ModelViewSet):
    queryset = models.Ingredient.objects.all()
    serializer_class = serializers.IngredientSerializer


class RecipeViewset(viewsets.ModelViewSet):
    queryset = models.Recipe.objects.all()

    def get_serializer_class(self):
        return serializers.RecipeSerializer
