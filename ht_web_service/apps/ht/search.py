from elasticsearch_dsl.connections import connections
from elasticsearch_dsl import DocType, Text, Date, Search
from elasticsearch_dsl.query import MultiMatch, Match, Q, MoreLikeThis, FuzzyLikeThis
from elasticsearch.helpers import bulk
from elasticsearch import Elasticsearch
from . import models

connections.create_connection()


class FeatureIndex(DocType):
    district = Text()
    order = Text()
    event = Text()
    piquetu = Text()
    plot = Text()
    rights_14 = Text()
    rights_17 = Text()
    cadastral_num_origin_14 = Text()
    cadastral_num_origin_17 = Text()
    origin_area_17 = Text()
    vac_area_14 = Text()
    vac_area_17 = Text()
    category_origin = Text()
    obj_type_origin = Text()
    cadastral_num_formed = Text()
    provision_doc = Text()
    requisites_dir_vac = Text()
    requisites_assess = Text()
    obj_costat = Text()
    offer_to_holdering = Text()
    requisites_agree_vac = Text()
    pre_doc_transfer_type = Text()
    prov_doc_FDA = Text()
    requisites_lease = Text()
    requisites_lease_agree = Text()
    contacts_holder = Text()
    comments = Text()
    form_area = Text()
    status_area = Text()
    rights_august_14 = Text()
    pre_lang_plan = Text()

    class Meta:
        index = 'feature-index'


def bulk_indexing():
    FeatureIndex.init()
    es = Elasticsearch()
    bulk(client=es, actions=(b.indexing() for b in models.Feature.objects.all().iterator()))


def search(query):
    # q = Q("multi_match", query=query)
    # q = Q(MoreLikeThis(like=query, fields=['order', 'id', 'event']))
    # q = Q({"query": {
    #     "more_like_this": {
    #         "like": query,
    #         "min_term_freq": 1,
    #         "max_query_terms": 12,
    #         "fields": ["event", "order"],
    #     }
    # }
    # })
    # # s = Search().query(MoreLikeThis(like=query, fields=['order', 'id']))
    # s = Search().query(q)
    # response = s[0:1000].execute()
    # print(response)
    es = Elasticsearch()
    res = es.search(index="feature-index",
                    body={"query": {
                            "query_string": {
                                "query": "*{}*".format(query),
                                "fields": ['event', 'order'],
                            }
                        },
                        'size': 1000,
                    })
    print(res['hits'])
    return res['hits']
