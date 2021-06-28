from datetime import timedelta

from django.test import TestCase
from django.utils import timezone

from alias.models import Alias
from alias.serializers import AliasSerializer


class AliasSerializerTestCase(TestCase):
    def setUp(self):
        self.start_alias_1 = timezone.now().replace(tzinfo=None).isoformat()
        self.end_alias_1 = (timezone.now() + timedelta(days=1)).replace(tzinfo=None).isoformat()

        self.start_alias_2 = timezone.now().replace(tzinfo=None).isoformat()
        self.end_alias_2 = (timezone.now() + timedelta(days=2)).replace(tzinfo=None).isoformat()

        self.start_alias_3 = (timezone.now() + timedelta(days=1)).replace(tzinfo=None).isoformat()
        self.end_alias_3 = (timezone.now() + timedelta(days=2)).replace(tzinfo=None).isoformat()

        self.start_alias_4 = timezone.now().replace(tzinfo=None).isoformat()
        self.end_alias_4 = (timezone.now() - timedelta(days=2)).replace(tzinfo=None).isoformat()

        self.alias_1 = Alias.objects.create(alias='alias_1',
                                            target='target_1',
                                            start=self.start_alias_1,
                                            end=self.end_alias_1
                                            )
        self.alias_2 = Alias.objects.create(alias='alias_2',
                                            target='target_2',
                                            start=self.start_alias_2,
                                            end=self.end_alias_2
                                            )
        self.alias_3 = Alias.objects.create(alias='alias_2',
                                            target='target_2',
                                            start=self.start_alias_3,
                                            )
        self.alias_4 = Alias.objects.create(alias='alias_2',
                                            target='target_2',
                                            start=self.start_alias_4,
                                            end=None
                                            )

    def test_serializer(self):
        data = AliasSerializer([self.alias_1, self.alias_2, self.alias_3, self.alias_4], many=True).data
        print(data[-1])
        expected_data = [
            {
                'id': self.alias_1.id,
                'alias': 'alias_1',
                'target': 'target_1',
                'start': self.start_alias_1,
                'end': self.end_alias_1
            },
            {
                'id': self.alias_2.id,
                'alias': 'alias_2',
                'target': 'target_2',
                'start': self.start_alias_2,
                'end': self.end_alias_2
            },
            {
                'id': self.alias_3.id,
                'alias': 'alias_2',
                'target': 'target_2',
                'start': self.start_alias_3,
                'end': None
            },
            {
                'id': self.alias_4.id,
                'alias': 'alias_2',
                'target': 'target_2',
                'start': self.start_alias_4,
                'end': None
            },
        ]
        print(expected_data[-1])
        self.assertEqual(expected_data, data)
