from rest_framework import serializers
from PDTinv.models import Tire


class TireSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tire
        fields = [  
			'width',
			'sidewall',
			'rim',
			'full_size',
				
        ]
        read_only_fields = ['full_size']