import os
import traceback
from db_helper.data_access import DataAccess
from app import app
import logging
import urllib.request
from werkzeug.utils import secure_filename
from flask import Flask, flash, jsonify, request, redirect, url_for, render_template
from flask_cors import CORS
logging.basicConfig(level=logging.INFO)
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])

curr_dir = os.getcwd()
#UPLOAD_FOLDER = curr_dir+'/TestApplication/uploads'


app.config['CORS_HEADERS'] = ['Content-Type']
app.config['CORS_SUPPORTS_CREDENTIALS']= True
cors = CORS(app, resources={r"/Ecommerce/*":{"origins":"*"}})

@app.route('/')
def upload_form():
    return 'Hello World'



@app.route('/Ecommerce/MenuHeader', methods=['GET'])
def get_menu_header():
    #img_url = url_for('static', filename=os.path.join('test_docs', choice(names)))
    logging.info("welcome to menu header")
    try:
        dal = DataAccess()
        result = dal.get_menu_header();
        response = jsonify({'status': 'success','result':result})
    except Exception as e:
        traceback.print_exc()
        response = jsonify({'status': 'failure', 'result': e})
        return response, 500
    return response, 200


@app.route('/Ecommerce/Site_Admin/Menu', methods=['GET'])
def get_menu_items():
    #img_url = url_for('static', filename=os.path.join('test_docs', choice(names)))
    logging.info("welcome to menu items")
    try:
        dal = DataAccess()
        result = dal.get_menu_items()
        all_menu_items_dict = {}
        unique_sub_id = {}
        for item_dict in result:
            all_menu_items_dict[item_dict['Menu_ID']] = item_dict
        if item_dict['Has_SubMenu'] == 1:
            unique_sub_id[item_dict['SubMenu_Menu_ID']] = item_dict['Menu_ID']
        
        print(unique_sub_id)    
        for key, val in all_menu_items_dict.items():
            if val['Has_SubMenu'] == 1:
                val['Sub_Menu'] = all_menu_items_dict[val['SubMenu_Menu_ID']]

        for i in unique_sub_id:
            all_menu_items_dict.pop(i)
        # data=dal.get_menu_items()
        # logging.info(data)
        # for i in data:
        #     dal = DataAccess()
        #     if i['has_submenu'] == 1:
        #         data= dal.get_submenu_items(i['submenu_menu_id'])
        #         logging.info(data)
        #         i.update({'Submenu':[i['submenu_menu_id']]})
        
        # print(data)
        # result = data
        #logging.info(result)
        response = jsonify({'status': 'success','result':result})
    except Exception as e:
        traceback.print_exc()
        response = jsonify({'status': 'failure', 'result': e})
        return response, 500
    return response, 200


@app.route('/Ecommerce/Site_Admin/Common', methods=['GET'])
def get_common():
    #img_url = url_for('static', filename=os.path.join('test_docs', choice(names)))
    logging.info("welcome to common")
    try:
        result = [{
            "topheader":{
           "h1text": "Children's Furniture",
           "ptext": "For children and adults, from the classic to the most innovative",
           "bannerpercent": "50%",
           "stext1": "Until",
           "stext2": "off",
		   "Active_Status" : 'true'
       }
        }]
        response = jsonify({'status': 'success','result':result})
    except Exception as e:
        traceback.print_exc()
        response = jsonify({'status': 'failure', 'result': e})
        return response, 500
    return response, 200
@app.route('/Ecommerce/Site_Admin/Advertisement', methods=['GET'])
def get_advertisement():
    #img_url = url_for('static', filename=os.path.join('test_docs', choice(names)))
    logging.info("welcome to common")
    try:
        result = [
        {
            "id": 1,
            "title": "repellendus id ullam",
            "label": "Dolorem officiis temporibus.",
            "url1": "https://abc.com"
        }
        ]
        response = jsonify({'status': 'success','result':result})
    except Exception as e:
        traceback.print_exc()
        response = jsonify({'status': 'failure', 'result': e})
        return response, 500
    return response, 200



@app.route('/Ecommerce/getProduct', methods=['GET'])
def get_product():
    #img_url = url_for('static', filename=os.path.join('test_docs', choice(names)))
    logging.info("welcome to product")
    try:
        dal = DataAccess()
        result = dal.get_product_details();
        for i in result:
            dal = DataAccess()
            data1=dal.get_product_images(i['product_id'])
            dal = DataAccess()
            data2=dal.get_product_features(i['product_id'])

            print(data1)
            i.update({'imageurls': data1})
            i.update({'features': data2})

        response = jsonify({'status': 'success','result':result})
    except Exception as e:
        traceback.print_exc()
        response = jsonify({'status': 'failure', 'result': e})
        return response, 500
    return response, 200


@app.route('/Ecommerce/getProduct/<product_id>', methods=['GET'])
def get_product_by_id(product_id):
    #img_url = url_for('static', filename=os.path.join('test_docs', choice(names)))
    logging.info("welcome to product")
    try:
        dal = DataAccess()
        result = dal.get_product_details_by_id(product_id);
        for i in result:
            dal = DataAccess()
            data1=dal.get_product_images(i['product_id'])
            dal = DataAccess()
            data2=dal.get_product_features(i['product_id'])

            print(data1)
            i.update({'imageurls': data1})
            i.update({'features': data2})

        response = jsonify({'status': 'success','result':result})
    except Exception as e:
        traceback.print_exc()
        response = jsonify({'status': 'failure', 'result': e})
        return response, 500
    return response, 200




if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port='8081', threaded=True)
