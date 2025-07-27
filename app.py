
from flask import Flask, request, jsonify, session
from collections import defaultdict
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Needed for session tracking

# In-memory data (use a database for production)
account_counts = defaultdict(int)
user_events = []  # List of dicts: {timestamp, event, version, user_id}

def log_event(event, version=None, user_id=None):
    user_events.append({
        'timestamp': datetime.utcnow().isoformat(),
        'event': event,
        'version': version,
        'user_id': user_id
    })

@app.route('/api/visit', methods=['POST'])
def visit():
    data = request.json
    version = data.get('version', 'A')
    user_id = session.get('user_id')
    log_event('visit', version, user_id)
    return jsonify({'success': True})

@app.route('/api/create-account', methods=['POST'])
def create_account():
    data = request.json
    version = data.get('version', 'A')  # 'A' or 'B'
    user_id = data.get('email')
    account_counts[version] += 1
    log_event('register', version, user_id)
    # Here you would save the account info to a database
    return jsonify({"success": True, "version": version, "count": account_counts[version]})

@app.route('/api/stats', methods=['GET'])
def stats():
    return jsonify({
        'account_counts': dict(account_counts),
        'user_events': user_events
    })

if __name__ == '__main__':
    app.run(debug=True)
