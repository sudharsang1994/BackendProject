
import logging
from db_helper.db_engine import DBEngine

class DataAccess(object):
    def __init__(self) -> None:
       self.db_eng = DBEngine()


    def get_menu_header(self):
        query='SELECT * FROM sakila.SITE_HEADER'
        return self.get_data_from_query(query)

    def get_menu_items(self):
        query='SELECT * FROM sakila.menu_items'
        return self.get_data_from_query(query)


    def format_menu_items(self):
        data=self.get_menu_items()
        for i in data:
            if i['has_submenu'] == 1:
                dal= DataAccess()
                data1= dal.get_submenu_items(i['submenu_menu_id'])
                i.update({'Submenu':data1})
        return data 

    def get_submenu_items(self, submenuid):
        logging.info(submenuid)
        query=f'SELECT * FROM sakila.menu_items where menu_id = {submenuid}'
        return self.get_data_from_query(query)


    def get_product_details(self):
        query='SELECT * FROM sakila.PRODUCT'
        return self.get_data_from_query(query)

    def get_product_details_by_id(self, product_id):
        query=f'SELECT * FROM sakila.PRODUCT where product_id = {product_id}'
        return self.get_data_from_query(query)

    def get_product_images(self, product_id):
        query= f'SELECT main_image,front_image,right_image,left_image,back_image from sakila.product_images where product_id ={product_id} '
        return self.get_data_from_query(query)

    def get_product_features(self, product_id):
        query= f'SELECT powersource,brand,modelname,specialfeature,description from sakila.product_features where product_id ={product_id} '
        return self.get_data_from_query(query)

    def get_data_from_query(self, query):
        data, column_names = self.db_eng.execute_query(query, get_columns=True)
        #logging.info(data)
        result = [dict(zip(column_names, row)) for row in data]
        return result

