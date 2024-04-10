from flask import Blueprint, request, jsonify
from db import execute_read_query, execute_write_query
import pandas as pd

bp = Blueprint('routes', __name__)


@bp.route('/sales', methods=['GET'])
def get_sales():
    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')
    response_format = request.args.get('format', 'json')

    if not start_date or not end_date:
        return jsonify({'error': 'Please provide start_date and end_date'}), 400

    query = """
        SELECT * FROM storedata.sales
        WHERE date BETWEEN %s AND %s;
    """
    result = execute_read_query(query, (start_date, end_date))

    df = pd.DataFrame(result)

    if response_format == 'list':
        return jsonify(df.to_dict(orient='records'))
    elif response_format == 'pandas':
        return df.to_json(orient='split')
    else:
        return jsonify(df.to_dict(orient='index'))


@bp.route('/sales', methods=['POST'])
def add_sale():
    data = request.get_json()

    if not data:
        return jsonify({'error': 'Please provide sale data'}), 400

    required_fields = ['id', 'store_id', 'total_sales', 'date']
    if not all(field in data for field in required_fields):
        return jsonify({'error': 'Missing data in request'}), 400

    query = """
        INSERT INTO storedata.sales (id, store_id, total_sales, date)
        VALUES (%s, %s, %s, %s);
    """
    try:
        execute_write_query(query, (data['id'], data['store_id'], data['total_sales'], data['date']))
        return jsonify({'message': "Sale added successfully"}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500
