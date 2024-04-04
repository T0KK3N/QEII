from flask import Flask, render_template, request, jsonify

app = Flask(__name__, static_url_path='/static')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate_order', methods=['POST'])
def calculate_order():
    # Retrieve data from the request
    data = request.json

    # Extract data from the request
    customer_id = int(data['customer'])
    quantity_A = int(data['product-a'])
    quantity_B = int(data['product-b'])
    quantity_C = int(data['product-c'])
    quantity_D = int(data['product-d'])

    # Product details
    products = {
        'A': {'unit_cost': 0.52, 'markup': 0.8, 'promotion': 0},
        'B': {'unit_cost': 0.38, 'markup': 1.2, 'promotion': 0.3},
        'C': {'unit_cost': 0.41, 'markup': 0.9, 'promotion': 0},
        'D': {'unit_cost': 0.60, 'markup': 1, 'promotion': 0.2}
    }

    # Calculate unit prices
    unit_prices = {}
    for product, details in products.items():
        if product in ['A', 'B']:
            unit_price = details['unit_cost'] + details['unit_cost'] * details['markup']
            if product == 'B':  # Apply promotion only for product B
                unit_price -= unit_price * details['promotion']
        else:
            unit_price = details['unit_cost'] + details['markup']
            if product == 'D':  # Apply promotion only for product D
                unit_price -= unit_price * details['promotion']
    
        unit_prices[product] = round(unit_price, 2)

    # Calculate line totals
    line_totals = {}
    for product, quantity in {'A': quantity_A, 'B': quantity_B, 'C': quantity_C, 'D': quantity_D}.items():
        line_totals[product] = quantity * unit_prices[product]

    # Calculate total amount before discounts
    total_amount_before_discounts = sum(line_totals.values())

    # Calculate Basic Customer Discount
    basic_discounts = {1: 0.05, 2: 0.04, 3: 0.03, 4: 0.02, 5: 0}
    basic_discount = basic_discounts.get(customer_id, 0)
    basic_discount_amount = total_amount_before_discounts * basic_discount

    # Calculate total amount after basic discount
    total_amount_after_basic_discount = total_amount_before_discounts - basic_discount_amount

    # Calculate Additional Bulk Discount
    bulk_discounts = {1: {10000: 0, 30000: 0.02}, 2: {10000: 0.01, 30000: 0.02}, 3: {10000: 0.01, 30000: 0.03}, 
                      4: {10000: 0.03, 30000: 0.05}, 5: {10000: 0.05, 30000: 0.07}}
    
    bulk_discount = 0
    if total_amount_after_basic_discount > 30000:
        bulk_discount = bulk_discounts.get(customer_id, {}).get(30000, 0)
    elif total_amount_after_basic_discount > 10000:
        bulk_discount = bulk_discounts.get(customer_id, {}).get(10000, 0)
    
    bulk_discount_amount = total_amount_after_basic_discount * bulk_discount

    # Calculate total amount after discounts
    total_amount_after_discounts = total_amount_after_basic_discount - bulk_discount_amount
    
    # Prepare the response data
    response_data = {
        'customerId': customer_id,
        'productA': quantity_A,
        'productB': quantity_B,
        'productC': quantity_C,
        'productD': quantity_D,
        'unitPrices': unit_prices,   # Include unit prices
        'lineTotals': line_totals,   # Include line totals
        'totalBeforeDiscounts': round(total_amount_before_discounts, 2),
        'totalAfterDiscounts': round(total_amount_after_discounts, 2)
    }

    # Return the response as JSON
    return jsonify(response_data)

if __name__ == '__main__':
    app.run(debug=True)