import json
from datetime import timedelta

from django.utils import timezone
from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse

from alias.models import Alias
from alias.serializers import AliasSerializer


class AliasApiTestCase(APITestCase):
    def setUp(self):
        self.start_alias_1 = timezone.now()
        self.end_alias_1 = timezone.now() + timedelta(days=1)

        self.start_alias_2 = timezone.now()
        self.end_alias_2 = timezone.now() + timedelta(days=2)

        self.start_alias_3 = timezone.now() + timedelta(days=1)
        self.end_alias_3 = timezone.now() + timedelta(days=2)

        self.start_alias_4 = timezone.now()
        self.end_alias_4 = timezone.now() - timedelta(days=2)

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
                                            end=self.end_alias_3
                                            )
        self.alias_4 = Alias.objects.create(alias='alias_1',
                                            target='alias_1',
                                            start=self.start_alias_4,
                                            end=self.end_alias_4
                                            )

    def test_get(self):
        url = reverse('alias-list')
        response = self.client.get(url)
        serializer_data = AliasSerializer([self.alias_1, self.alias_2, self.alias_3, self.alias_4], many=True).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)

    def test_get_alias(self):
        url = reverse('alias-detail', args=(self.alias_1.id,))
        response = self.client.get(url)
        serializer_data = AliasSerializer(self.alias_1).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)

    def test_get_filter(self):
        url = reverse('alias-list')
        response = self.client.get(url, data={'alias': 'alias_2'})
        serializer_data = AliasSerializer([self.alias_2, self.alias_3], many=True).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)

    def test_get_search(self):
        url = reverse('alias-list')
        response = self.client.get(url, data={'search': 'alias_1'})
        serializer_data = AliasSerializer([self.alias_1, self.alias_4], many=True).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)

    def test_get_ordering(self):
        url = reverse('alias-list')
        response = self.client.get(url, data={'ordering': 'alias'})
        serializer_data = AliasSerializer([self.alias_1, self.alias_4, self.alias_2, self.alias_3], many=True).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)

    def test_post(self):
        self.assertEqual(4, Alias.objects.all().count())
        url = reverse('alias-list')
        data = {'alias': 'alias_2',
                'target': 'target_3',
                'start': f'{timezone.now()}',
                'end': f'{timezone.now() + timedelta(days=2)}'
                }
        json_data = json.dumps(data)
        response = self.client.post(url, data=json_data, content_type='application/json')

        self.assertEqual(status.HTTP_201_CREATED, response.status_code)
        self.assertEqual(5, Alias.objects.all().count())

    def test_put(self):
        url = reverse('alias-detail', args=(self.alias_1.id,))
        data = {'alias': 'alias_5',
                'target': self.alias_1.target,
                'start': f'{timezone.now()}',
                'end': f'{timezone.now() + timedelta(days=2)}'
                }
        json_data = json.dumps(data)
        response = self.client.put(url, data=json_data, content_type='application/json')
        self.alias_1.refresh_from_db()

        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual('alias_5', self.alias_1.alias)

    def test_del(self):
        self.assertEqual(4, Alias.objects.all().count())
        url = reverse('alias-detail', args=(self.alias_1.id,))
        response = self.client.delete(url)

        self.assertEqual(status.HTTP_204_NO_CONTENT, response.status_code)
        self.assertEqual(3, Alias.objects.all().count())
