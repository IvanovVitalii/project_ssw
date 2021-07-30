import datetime

from django.db.models import Q
from rest_framework.serializers import ModelSerializer, ValidationError

from alias.models import Alias


class AliasSerializer(ModelSerializer):
    class Meta:
        model = Alias
        fields = '__all__'

    def validate(self, data):
        '''Validate data in accordance with the requirements of the task'''
        data_db = Alias.objects.filter(Q(alias=data['alias']) & Q(target=data['target']))
        # there is a request option without the 'end' field
        try:
            data['end']
        except KeyError as e:
            data['end'] = None
        data_start = data['start']
        # replace 'None' with 'datetime.datetime.max'
        if data['end'] is None:
            data_end = datetime.datetime.max
        else:
            data_end = data['end']
        if data_start > data_end:
            raise ValidationError("End must occur after start")
        # Further, the check is incorrect. I think how to decide correctly
        if data_db:
            start_set = [x.start for x in data_db]
            end_set = [x.end for x in data_db]
            for start in start_set:
                for end in end_set:
                    if end is None:
                        end = datetime.datetime.max
                    if start <= data_start <= end or start >= data_end >= end:
                        raise ValidationError("Incorrect DateTime")
        return data
