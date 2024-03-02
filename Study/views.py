from rest_framework import viewsets
from rest_framework.response import Response
from django.db.models import Count
from django.utils import timezone
from .models import Product, Lesson, Group
from .serializers import ProductSerializer, LessonSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def distribute_users_to_groups(self, product):
        if product.start_datetime > timezone.now():

            groups = Group.objects.filter(product=product).annotate(num_members=Count('members'))

            min_users = product.min_users
            max_users = product.max_users
            
            groups = groups.order_by('num_members')
            

            users_to_distribute = product.members.all()
            for group in groups:
 
                if group.num_members < max_users:

                    users_in_group = users_to_distribute[:max_users - group.num_members]
                    group.members.add(*users_in_group)

                    users_to_distribute = users_to_distribute[max_users - group.num_members:]
                    if len(users_to_distribute) == 0:
                        break

            while len(users_to_distribute) > 0:
                new_group = Group.objects.create(title=f"{product.title} Group",
                                                product=product)
                users_in_group = users_to_distribute[:max_users]
                new_group.members.add(*users_in_group)
                users_to_distribute = users_to_distribute[max_users:]

class LessonViewSet(viewsets.ModelViewSet):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
