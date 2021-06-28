from datetime import timedelta

from django.db.models import Q
from django.utils import timezone
from rest_framework.serializers import ModelSerializer, ValidationError

from alias.models import Alias


class AliasSerializer(ModelSerializer):
    class Meta:
        model = Alias
        fields = '__all__'

    def validate(self, data):
        data_db = Alias.objects.filter(Q(alias=data['alias']) & Q(target=data['target']))
        try:
            data['end']
        except KeyError as e:
            data['end'] = None
        data_start = data['start']
        if data['end'] is None:
            data_end = timezone.now() + timedelta(days=10 ** 2)
        else:
            data_end = data['end']
        if data_start > data_end:
            raise ValidationError("End must occur after start")
        if data_db:
            start_set = [x.start for x in data_db]
            end_set = [x.end for x in data_db]
            for start in start_set:
                for end in end_set:
                    if end is None:
                        end = timezone.now() + timedelta(days=10 ** 2)
                    if start <= data_start <= end or start >= data_end >= end:
                        raise ValidationError("Incorrect DateTime")
        return data
