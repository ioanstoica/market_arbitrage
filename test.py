import unittest
import aliexpress
import olx

class MyTestCase(unittest.TestCase):
    def test_set_pret_aliexpress(self):
        url_produs = "https://www.aliexpress.com/item/1005005583051432.html?spm=a2g0o.detail.0.0.6ea0156cQs8IeL&gps-id=pcDetailTopMoreOtherSeller&scm=1007.40000.327270.0&scm_id=1007.40000.327270.0&scm-url=1007.40000.327270.0&pvid=996e1924-26ca-46d6-9d09-89e407fe207a&_t=gps-id:pcDetailTopMoreOtherSeller,scm-url:1007.40000.327270.0,pvid:996e1924-26ca-46d6-9d09-89e407fe207a,tpp_buckets:668%232846%238113%231998&pdp_npi=4%40dis%21RON%2173.57%212.35%21%21%21112.37%21%21%402101fb0d16988725005753254e4578%2112000033675122453%21rec%21RO%214741553500%21AB"
        oferta = aliexpress.AliexpresssOferta(url = url_produs)
        oferta.find_pret()
        self.assertEqual(oferta.pret, "RON2.35")

    def test_find_olx(self):
        url_produs = "https://www.olx.ro/d/oferta/tesla-model-3-long-range-363-cai-77-000-km-tva-deductibil-2019-IDhcQIa.html"
        oferta = olx.OlxOferta(url = url_produs)
        oferta.complete_fields()
        self.assertEqual(oferta.id, "254260274")
        self.assertEqual(oferta.views, "2651")
        self.assertEqual(oferta.photo_urls[0][0:35], 
                         "https://frankfurt.apollo.olxcdn.com")
        self.assertEqual(len(oferta.photo_urls), 4)
        


if __name__ == '__main__':
    unittest.main()