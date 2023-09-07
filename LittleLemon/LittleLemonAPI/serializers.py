from .models import MenuItem, Category
from rest_framework import serializers

class CategorySerializer(serializers.ModelSerializer):
    class Meta():
        model = Category
        fields = ['id','title']


class MenuItemSerializer(serializers.ModelSerializer):
    #category_id = serializers.IntegerField(write_only=True)
    #category = CategorySerializer(read_only=True)
    class Meta():
        model = MenuItem
        fields = ['id','title','price','inventory']
        extra_kwargs = {'price':{'min_value':1},
                        'inventory':{'min_value':0}}
        
