from flask import Flask, request, jsonify

app = Flask(__name__)

# Initialize user's points balance
transactions = []


# Define the route for adding points
@app.route('/add', methods=['POST'])
def add_points():
    global transactions
    # Get the request body
    data = request.get_json()
    # Check if all required fields are present in the request
    if 'payer' not in data or 'points' not in data or 'timestamp' not in data:
        return jsonify({'error': 'Payer, points, and timestamp are required fields'}), 400

    # Add the transaction to the list of transactions
    transactions.append(data)
    # Return a success end code 200
    return '', 200

# Define the route for spending points
@app.route('/spend', methods=['POST'])
def spend_points():
    # Get the points to spend from the request body
    global transactions
    data = request.get_json()
    points_to_spend = data.get('points', 0)

    # Calculate the total points available
    total_points = sum(transaction['points'] for transaction in transactions)

    # Check if the user has enough points to spend
    if points_to_spend > total_points:
        return 'User does not have enough points', 400

    # Sort transactions by timestamp (oldest first)
    transactions.sort(key=lambda x: x['timestamp'])

    # Initialize variables to track spent points
    spent_points = points_to_spend
    spent_transactions = []

    # Iterate through transactions to spend points
    for transaction in transactions:
        points = transaction['points']
        payer = transaction['payer']

        # Calculate how many points to spend from this transaction
        points_to_deduct = min(points, spent_points)

        # Update the transaction's points
        transaction['points'] -= points_to_deduct

        # Update the spent points and add to the response list
        spent_points -= points_to_deduct
        spent_transactions.append({'payer': payer, 'points': -points_to_deduct})

        # If all points are spent, break the loop
        if spent_points == 0:
            break

    # Respond with the list of spent transactions
    return jsonify(spent_transactions), 200

# Define the route for getting points balance
@app.route('/balance', methods=['GET'])
def get_points_balance():
    global transactions
    # Initialize a dictionary to store points balance
    points_balance = {}

    # Iterate through transactions to calculate points balance
    for transaction in transactions:
        payer = transaction['payer']
        points = transaction['points']

        # Add payer to points balance if not present
        if payer not in points_balance:
            points_balance[payer] = 0

        # Update the points balance
        points_balance[payer] += points

    # Return the points balance
    return jsonify(points_balance), '200'

if __name__ == '__main__':
    app.run(port=8000)