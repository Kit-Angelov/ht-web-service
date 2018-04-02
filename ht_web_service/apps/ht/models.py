from django.db import models
from ht_web_service.users.models import User as CustomUser
from .search import FeatureIndex


class Feature(models.Model):
    district = models.CharField(max_length=56, blank=True, null=True, verbose_name="Район")
    order = models.CharField(max_length=256, blank=True, null=True, verbose_name="№ п/п")
    event = models.CharField(max_length=256, blank=True, null=True, verbose_name="Мероприятие")
    piquetu = models.CharField(max_length=256, blank=True, null=True, verbose_name="Пикет")
    plot = models.CharField(max_length=256, blank=True, null=True, verbose_name="№ зу ПМТ")
    rights_14 = models.CharField(max_length=256, blank=True, null=True, verbose_name="Права ПМТ 2014")
    rights_17 = models.CharField(max_length=256, blank=True, null=True, verbose_name="Права ПМТ 2017")
    cadastral_num_origin_14 = models.CharField(max_length=256, blank=True, null=True, verbose_name="Кадастровый номер исходного объекта недвижимости ПМТ 2014")
    cadastral_num_origin_17 = models.CharField(max_length=256, blank=True, null=True, verbose_name="Кадастровый номер исходного объкта недвижимости ПМТ 2017")
    origin_area_17 = models.CharField(max_length=256, blank=True, null=True, verbose_name="Площадь исходного объекта недвижимости, кв.м. ПМТ 2017")
    vac_area_14 = models.CharField(max_length=256, blank=True, null=True, verbose_name="Площадь подлежащая изъятию, кв.м. ПМТ 2014")
    vac_area_17 = models.CharField(max_length=256, blank=True, null=True, verbose_name="Площадь подлежащая изъятию, кв.м. ПМТ 2017")
    category_origin = models.CharField(max_length=256, blank=True, null=True, verbose_name="Категория исходного объекта недвижимости")
    obj_type_origin = models.CharField(max_length=256, blank=True, null=True, verbose_name="ВРИ исходного объекта недвижимости")
    cadastral_num_formed = models.CharField(max_length=256, blank=True, null=True, verbose_name="Кадастровый номер образованного объекта недвижимости")
    provision_doc = models.CharField(max_length=256, blank=True, null=True, verbose_name="Предоставление документов для подготовки распоряжения ФДА об изъятии")
    requisites_dir_vac = models.CharField(max_length=256, blank=True, null=True, verbose_name="Реквизиты распоряжения об изъятии")
    requisites_assess = models.CharField(max_length=256, blank=True, null=True, verbose_name="Реквизиты отчета об оценке")
    obj_costat = models.CharField(max_length=256, blank=True, null=True, verbose_name="Стоимость объектов недвижимости")
    offer_to_holdering = models.CharField(max_length=256, blank=True, null=True, verbose_name="Направление оферты правообладателю")
    requisites_agree_vac = models.CharField(max_length=256, blank=True, null=True, verbose_name="Реквизиты соглашения об изъятии ")
    pre_doc_transfer_type = models.CharField(max_length=256, blank=True, null=True, verbose_name="Подготовка документов для перевода (отнесения) в категорию земель транспорта и/или изменение (установление) ВРИ")
    prov_doc_FDA = models.CharField(max_length=256, blank=True, null=True, verbose_name="Предоставление документов для подготовки распоряжения ФДА о предоставлении в аренду ")
    requisites_lease = models.CharField(max_length=256, blank=True, null=True, verbose_name="Реквизиты распоряжения о предоставлении в аренду")
    requisites_lease_agree = models.CharField(max_length=256, blank=True, null=True, verbose_name="Реквизиты договора аренды")
    contacts_holder = models.CharField(max_length=256, blank=True, null=True, verbose_name="Контакты правообладателя")
    comments = models.CharField(max_length=256, blank=True, null=True, verbose_name="Комментарий")
    form_area = models.CharField(max_length=256, blank=True, null=True, verbose_name="Формирование земельных участков (кадастровый учет)")
    status_area = models.CharField(max_length=256, blank=True, null=True, verbose_name="Статус участка")
    rights_august_14 = models.CharField(max_length=256, blank=True, null=True, verbose_name="Право после августа 2014")
    pre_lang_plan = models.CharField(max_length=256, blank=True, null=True, verbose_name="Подготовка межевого плана и передача его на кадастровый учет")

    def indexing(self):
        obj = FeatureIndex(
            meta={'id': self.id},
            order=self.order,
            event=self.event,
            piquetu=self.piquetu,
            district=self.district,
            plot=self.plot,
            rights_14=self.rights_14,
            rights_17=self.rights_17,
            cadastral_num_origin_14=self.cadastral_num_origin_14,
            cadastral_num_origin_17=self.cadastral_num_origin_17,
            origin_area_17=self.origin_area_17,
            vac_area_14=self.vac_area_14,
            vac_area_17=self.vac_area_17,
            category_origin=self.category_origin,
            obj_type_origin=self.obj_type_origin,
            cadastral_num_formed=self.cadastral_num_formed,
            provision_doc=self.provision_doc,
            requisites_dir_vac=self.requisites_dir_vac,
            requisites_assess=self.requisites_assess,
            obj_costat=self.obj_costat,
            offer_to_holdering=self.offer_to_holdering,
            requisites_agree_vac=self.requisites_agree_vac,
            pre_doc_transfer_type=self.pre_doc_transfer_type,
            prov_doc_FDA=self.prov_doc_FDA,
            requisites_lease=self.requisites_lease,
            requisites_lease_agree=self.requisites_lease_agree,
            contacts_holder=self.contacts_holder,
            comments=self.comments,
            form_area=self.form_area,
            status_area=self.status_area,
            rights_august_14=self.rights_august_14,
            pre_lang_plan=self.pre_lang_plan,
        )
        obj.save()
        return obj.to_dict(include_meta=True)


class History(models.Model):
    date = models.DateTimeField()
    feature = models.ForeignKey(Feature, on_delete=models.CASCADE)
    attribute = models.CharField(max_length=256)
    value = models.CharField(max_length=256)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return '{0}|{1}|{2}|{3}'.format(str(self.attribute), str(self.feature.id), str(self.user.id), str(self.date))


def get_attributes():
    machine_and_verbose_names_dict = dict()
    feature_fields = Feature._meta.fields
    for field in feature_fields:
        try:
            machine_and_verbose_names_dict[field.name] = field.verbose_name
        except Exception as e:
            print(e)

    return machine_and_verbose_names_dict
