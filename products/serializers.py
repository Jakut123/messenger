from rest_framework import serializers

from products.models import Product, Comment, Category, Like


class ProductsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name', 'price')


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = '__all__'

    def validate_rating(self, rating):
        if rating not in range(-1, 2):
            raise serializers.ValidationError('Только лайк или дизлайк! НЕ РЕЙТИНГ!')
        return rating


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['product', 'text', 'rating']

    def validate_rating(self, rating):
        if rating not in range(1, 6):
            raise serializers.ValidationError('Рейтинг должен быть от 1 до 5')
        return rating

    def create(self, validated_data):
        user = self.context['request'].user
        validated_data['author'] = user
        return super().create(validated_data)

#
# class OrderItemSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = OrderItem
#         fields = ['product', 'quantity']
#
#
# class OrderSerializer(serializers.ModelSerializer):
#     positions = OrderItemSerializer(write_only=True, many=True)
#     status = serializers.CharField(read_only=True)
#
#     class Meta:
#         model = Order
#         fields = ['id', 'created_at', 'positions', 'status']
#
#     def create(self, validated_data):
#         products = validated_data.pop('positions')
#         user = self.context.get('request').user
#         order = Order.objects.create(user=user, status='open')
#         for prod in products:
#             product = prod['product']
#             quantity = prod['quantity']
#             OrderItem.objects.create(order=order,
#                                      product=product,
#                                      quantity=quantity)
#         return order
#
#     def to_representation(self, instance):
#         representation = super().to_representation(instance)
#         representation['positions'] = OrderItemSerializer(instance.items.all(), many=True).data
#         return representation