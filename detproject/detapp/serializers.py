from rest_framework import serializers

from .models import detemployee

class adultSerializer(serializers.ModelSerializer):
    class Meta:
        model = detemployee
        # fields = ("age",'work','fwt','education','edu_no','marital_status','occupation',
        # 'relationship','race','sex','cap_gain','cap_loss','hours_pw','native_country','salary')
        fields = '__all__'
 