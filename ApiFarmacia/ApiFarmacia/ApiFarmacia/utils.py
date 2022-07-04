from rest_framework import serializers

def max_min_validator(value):
    if value < 0:
        raise serializers.ValidationError('El stock no puede ser negativo ingrese otro valor')
    else:
        return value