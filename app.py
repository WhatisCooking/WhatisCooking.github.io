# --- A/B Test Comparison & Recommendation ---
@app.route('/ab-comparison', methods=['GET'])
def ab_comparison():
    # Compare account creation counts for A and B
    count_a = account_counts.get('A', 0)
    count_b = account_counts.get('B', 0)
    recommendation = None
    if count_a > count_b:
        recommendation = 'Version A is recommended based on higher account creation.'
    elif count_b > count_a:
        recommendation = 'Version B is recommended based on higher account creation.'
    else:
        recommendation = 'Both versions performed equally. Consider further testing.'
    return render_template('ab-comparison.html', count_a=count_a, count_b=count_b, recommendation=recommendation)


import time
import random
from flask import Flask, request, jsonify, session, render_template, redirect, make_response
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

# --- A/B Test Landing ---
@app.route('/')
def ab_test_landing():
    """Randomly and fairly assign user to A/B landing page, persist in cookie."""
    version = request.cookies.get('landing_version')
    if version not in ['A', 'B']:
        version = random.choice(['A', 'B'])
    resp = make_response(redirect(f'/create-account-landing?version={version}'))
    resp.set_cookie('landing_version', version, max_age=60*60*24*30)  # 30 days
    return resp

@app.route('/create-account-landing')
def create_account_landing():
    version = request.args.get('version', 'A')
    if version == 'B':
        return render_template('create-account-b.html')
    return render_template('create-account.html')

# --- API: User Visit Tracking ---
@app.route('/api/visit', methods=['POST'])
def visit():
    data = request.json
    version = data.get('version', 'A')
    user_id = session.get('user_id')
    log_event('visit', version, user_id)
    return jsonify({'success': True})

# --- API: Account Creation Tracking ---
@app.route('/api/create-account', methods=['POST'])
def create_account():
    data = request.json
    version = data.get('version', 'A')  # 'A' or 'B'
    user_id = data.get('email')
    account_counts[version] += 1
    log_event('register', version, user_id)
    # Here you would save the account info to a database
    return jsonify({"success": True, "version": version, "count": account_counts[version]})

# --- API: Stats ---
@app.route('/api/stats', methods=['GET'])
def stats():
    return jsonify({
        'account_counts': dict(account_counts),
        'user_events': user_events
    })

# --- Analyze Product Page ---
@app.route('/analyze-product', methods=['GET', 'POST'])
def analyze_product():
    value_props = None
    audience = None
    competitors = None
    if request.method == 'POST':
        product_url = request.form.get('product-url')
        # Simple analysis logic (replace with real NLP/model)
        if product_url:
            value_props = f"Value props for {product_url}: High quality, affordable, innovative."
            audience = f"Target audience for {product_url}: Young professionals, tech-savvy users."
            competitors = f"Competitors for {product_url}: ExampleBrand, SampleCorp."
    return render_template('analyze-product.html', value_props=value_props, audience=audience, competitors=competitors)

# --- Set Targeting Criteria Page ---
@app.route('/set-targeting', methods=['GET', 'POST'])
def set_targeting():
    budget = None
    countries = None
    targeting_criteria = None
    if request.method == 'POST':
        budget = request.form.get('daily-budget')
        countries = request.form.getlist('countries')
        targeting_criteria = request.form.get('criteria')
    return render_template('set-targeting.html', budget=budget, countries=countries, targeting_criteria=targeting_criteria)


# --- Generate Creatives Page ---
@app.route('/generate-creatives', methods=['GET', 'POST'])
def generate_creatives():
    product_url = None
    creatives = None
    images = None
    value_props = None
    audience = None
    competitors = None
    if request.method == 'POST':
        product_url = request.form.get('product-url')
        # Use same analysis logic as analyze_product
        if product_url:
            value_props = f"High quality, affordable, innovative."
            audience = f"Young professionals, tech-savvy users."
            competitors = f"ExampleBrand, SampleCorp."
            creatives = [
                f"Ad Headline: Discover the best of {product_url}!",
                f"Ad Text: Experience {value_props} at {product_url}. Shop now!",
                f"Target Audience: {audience}",
                f"Competitors: {competitors}"
            ]
            # Simulate image generation based on analysis
            images = [
                {
                    'src': f'https://via.placeholder.com/400x200?text={product_url}+Ad+1',
                    'alt': f'Ad image for {product_url} featuring {value_props}'
                },
                {
                    'src': f'https://via.placeholder.com/400x200?text={product_url}+Ad+2',
                    'alt': f'Ad image for {product_url} targeting {audience}'
                }
            ]
    return render_template('generate-creatives.html', product_url=product_url, creatives=creatives, images=images)


# --- Draft Media Plan Page ---
@app.route('/draft-media-plan', methods=['GET', 'POST'])
def draft_media_plan():
    targeting = None
    timeline = None
    ad_sets = None
    if request.method == 'POST':
        targeting = request.form.get('targeting')
        # Simple logic to draft media plan (replace with real logic/model)
        if targeting:
            timeline = [
                {'phase': 'Launch', 'start': '2025-08-01', 'end': '2025-08-07'},
                {'phase': 'Optimization', 'start': '2025-08-08', 'end': '2025-08-21'},
                {'phase': 'Scale', 'start': '2025-08-22', 'end': '2025-08-31'}
            ]
            ad_sets = [
                {'name': 'Ad Set 1', 'audience': targeting, 'budget': '$500', 'duration': '7 days'},
                {'name': 'Ad Set 2', 'audience': targeting + ' + Lookalike', 'budget': '$700', 'duration': '14 days'}
            ]
    return render_template('draft-media-plan.html', targeting=targeting, timeline=timeline, ad_sets=ad_sets)

# --- Review Launch Page ---
@app.route('/review-launch', methods=['GET', 'POST'])
def review_launch():
    launched = False
    if request.method == 'POST':
        # Simulate campaign launch logic
        launched = True
        log_event('campaign_launched')
        time.sleep(1)  # Simulate processing delay
    return render_template('review-launch.html', launched=launched)

# --- Monitor Campaign Page ---
@app.route('/monitor-campaign', methods=['GET', 'POST'])
def monitor_campaign():
    # Filter user_events for campaign launch and related metrics
    launched_events = [e for e in user_events if e['event'] == 'campaign_launched']
    # Example: count launches and provide dummy metrics
    campaign_metrics = {
        'launch_count': len(launched_events),
        'impressions': 12500 * len(launched_events),
        'clicks': 1230 * len(launched_events),
        'ctr': '9.8%',
        'conversions': 210 * len(launched_events)
    }
    return render_template('monitor-campaign.html', campaign_metrics=campaign_metrics)



if __name__ == '__main__':
    app.run(debug=True)
