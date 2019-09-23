from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Property


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class PropertySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Property
        fields = ['x','y','pams_pin','municipal_code','block','lot','qualifier','prop_class','county','municipal_name','property_location','owner_name','owner_st_address','owner_city_state','owner_zip_code','land_val','imprvt_val','net_value','last_yr_tx','bldg_desc','land_desc','calc_acre','add_lots1','add_lots2','fac_name','prop_use','bldg_class','deed_book','deed_page','deed_date','yr_constr','sales_code','sale_price','dwell','comm_dwell','latitude','longitude','accuracy_score','accuracy_type','number','property_street','street','city','state','zipcode','source','summary','delivery_line_1','delivery_line_2','city_name','rdi','precision','dpv_match_code','dpv_footnotes','footnotes','zip_type','carrier_route','dpv_vacant','active','urbanization']