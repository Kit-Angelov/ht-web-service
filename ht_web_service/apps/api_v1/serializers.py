from ht_web_service.apps.ht.models import *
from ht_web_service.users.models import User as CustomUser
from rest_framework import serializers
from datetime import datetime


class FeatureSerializers(serializers.ModelSerializer):
    # url = serializers.HyperlinkedIdentityField(view_name="api_v1:feature-detail", )

    class Meta:
        model = Feature
        fields = '__all__'

    def update(self, instance, validated_data):
        self.changable_attributes = dict()

        instance.order = self.change(instance.order, validated_data.get('order', instance.order), 'order')
        instance.event = self.change(instance.event, validated_data.get('event', instance.event), 'event')
        instance.piquetu = self.change(instance.piquetu, validated_data.get('piquetu', instance.piquetu), 'piquetu')
        instance.district = self.change(instance.district, validated_data.get('district', instance.district), 'district')
        instance.plot = self.change(instance.plot, validated_data.get('plot', instance.plot), 'plot')
        instance.rights_14 = self.change(instance.rights_14, validated_data.get('rights_14', instance.rights_14), 'rights_14')
        instance.rights_17 = self.change(instance.rights_17, validated_data.get('rights_17', instance.rights_17), 'rights_17')
        instance.cadastral_num_origin_14 = self.change(instance.cadastral_num_origin_14, validated_data.get('cadastral_num_origin_14', instance.cadastral_num_origin_14), 'cadastral_num_origin_14')
        instance.cadastral_num_origin_17 = self.change(instance.cadastral_num_origin_17, validated_data.get('cadastral_num_origin_17', instance.cadastral_num_origin_17), 'cadastral_num_origin_17')
        instance.origin_area_17 = self.change(instance.origin_area_17, validated_data.get('origin_area_17', instance.origin_area_17), 'origin_area_17')
        instance.vac_area_14 = self.change(instance.vac_area_14, validated_data.get('vac_area_14', instance.vac_area_14), 'vac_area_14')
        instance.vac_area_17 = self.change(instance.vac_area_17, validated_data.get('vac_area_17', instance.vac_area_17), 'vac_area_17')
        instance.category_origin = self.change(instance.category_origin, validated_data.get('category_origin', instance.category_origin), 'category_origin')
        instance.obj_type_origin = self.change(instance.obj_type_origin, validated_data.get('obj_type_origin', instance.obj_type_origin), 'obj_type_origin')
        instance.cadastral_num_formed = self.change(instance.cadastral_num_formed, validated_data.get('cadastral_num_formed', instance.cadastral_num_formed), 'cadastral_num_formed')
        instance.provision_doc = self.change(instance.provision_doc, validated_data.get('provision_doc', instance.provision_doc), 'provision_doc')
        instance.requisites_dir_vac = self.change(instance.requisites_dir_vac, validated_data.get('requisites_dir_vac', instance.requisites_dir_vac), 'requisites_dir_vac')
        instance.requisites_assess = self.change(instance.requisites_assess, validated_data.get('requisites_assess', instance.requisites_assess), 'requisites_assess')
        instance.obj_costat = self.change(instance.obj_costat, validated_data.get('obj_costat', instance.obj_costat), 'obj_costat')
        instance.offer_to_holdering = self.change(instance.offer_to_holdering, validated_data.get('offer_to_holdering', instance.offer_to_holdering), 'offer_to_holdering')
        instance.requisites_agree_vac = self.change(instance.requisites_agree_vac, validated_data.get('requisites_agree_vac', instance.requisites_agree_vac), 'requisites_agree_vac')
        instance.pre_doc_transfer_type = self.change(instance.pre_doc_transfer_type, validated_data.get('pre_doc_transfer_type', instance.pre_doc_transfer_type), 'pre_doc_transfer_type')
        instance.prov_doc_FDA  = self.change(instance.prov_doc_FDA , validated_data.get('prov_doc_FDA ', instance.prov_doc_FDA ), 'prov_doc_FDA ')
        instance.requisites_lease = self.change(instance.requisites_lease, validated_data.get('requisites_lease', instance.requisites_lease), 'requisites_lease')
        instance.requisites_lease_agree = self.change(instance.requisites_lease_agree, validated_data.get('requisites_lease_agree', instance.requisites_lease_agree), 'requisites_lease_agree')
        instance.contacts_holder = self.change(instance.contacts_holder, validated_data.get('contacts_holder', instance.contacts_holder), 'contacts_holder')
        instance.comments = self.change(instance.comments, validated_data.get('comments', instance.comments), 'comments')
        instance.form_area = self.change(instance.form_area, validated_data.get('form_area', instance.form_area), 'form_area')
        instance.status_area = self.change(instance.status_area, validated_data.get('status_area', instance.status_area), 'status_area')
        instance.rights_august_14 = self.change(instance.rights_august_14, validated_data.get('rights_august_14', instance.rights_august_14), 'rights_august_14')
        instance.pre_lang_plan = self.change(instance.pre_lang_plan, validated_data.get('pre_lang_plan', instance.pre_lang_plan), 'pre_lang_plan')
        instance.save()

        for field_name in self.changable_attributes:
            history_instance = History(date=datetime.now(),
                                       feature=instance,
                                       attribute=field_name,
                                       value=self.changable_attributes[field_name],
                                       user=CustomUser.objects.all()[0]) #??????????????!!!!!!!!!!!
            history_instance.save()

        return instance

    def change(self, old_value, new_value, field_name):

        if old_value != new_value:
            self.changable_attributes[field_name] = new_value
            return new_value
        else:
            return old_value


class UserSerializers(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="api_v1:user-detail",)
    class Meta:
        model = CustomUser
        fields = ['id', 'url', 'username']


class HistorySerializers(serializers.ModelSerializer):

    user = UserSerializers()

    class Meta:
        model = History
        fields = ['id', 'date', 'feature_id', 'attribute', 'value', 'user']

