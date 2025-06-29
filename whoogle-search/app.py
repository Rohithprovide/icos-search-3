"""
Whoogle Search Flask Application
Privacy-focused search engine interface
"""

from flask import Flask, request, render_template, redirect, url_for, jsonify
import requests
from bs4 import BeautifulSoup
import os
import re
import urllib.parse
from datetime import datetime

app = Flask(__name__)
app.secret_key = os.urandom(24)

# Configuration
GOOGLE_URL = "https://www.google.com/search"
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"

class WhoogleSearch:
    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': USER_AGENT,
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
        })
    
    def search(self, query, start=0, num=10):
        """Perform search and return results"""
        params = {
            'q': query,
            'start': start,
            'num': num,
            'hl': os.getenv('WHOOGLE_CONFIG_LANGUAGE', 'en'),
            'gl': os.getenv('WHOOGLE_CONFIG_COUNTRY', 'US'),
            'safe': os.getenv('WHOOGLE_CONFIG_SAFE', 'off')
        }
        
        try:
            response = self.session.get(GOOGLE_URL, params=params, timeout=10)
            response.raise_for_status()
            return self.parse_results(response.text, query)
        except requests.RequestException as e:
            return {'error': f'Search request failed: {str(e)}', 'results': []}
    
    def parse_results(self, html, query):
        """Parse Google search results"""
        soup = BeautifulSoup(html, 'html.parser')
        results = []
        
        # Find search result containers
        result_containers = soup.find_all('div', class_='g')
        
        for container in result_containers:
            try:
                # Extract title
                title_elem = container.find('h3')
                if not title_elem:
                    continue
                title = title_elem.get_text(strip=True)
                
                # Extract URL
                link_elem = container.find('a')
                if not link_elem or not link_elem.get('href'):
                    continue
                url = link_elem['href']
                
                # Clean up URL if it's a Google redirect
                if url.startswith('/url?'):
                    url_params = urllib.parse.parse_qs(urllib.parse.urlparse(url).query)
                    url = url_params.get('q', [url])[0]
                
                # Extract description
                desc_elem = container.find('span', class_=['st', 'aCOpRe'])
                if not desc_elem:
                    desc_elem = container.find('div', class_=['s', 'st'])
                description = desc_elem.get_text(strip=True) if desc_elem else ''
                
                results.append({
                    'title': title,
                    'url': url,
                    'description': description
                })
                
            except Exception as e:
                continue
        
        return {
            'query': query,
            'results': results,
            'total_results': len(results)
        }

# Initialize search engine
search_engine = WhoogleSearch()

@app.route('/')
def index():
    """Main search page"""
    return render_template('index.html')

@app.route('/search')
def search():
    """Handle search requests"""
    query = request.args.get('q', '').strip()
    if not query:
        return redirect(url_for('index'))
    
    start = int(request.args.get('start', 0))
    results = search_engine.search(query, start=start)
    
    return render_template('results.html', 
                         query=query, 
                         results=results['results'],
                         error=results.get('error'),
                         start=start)

@app.route('/api/search')
def api_search():
    """API endpoint for search"""
    query = request.args.get('q', '').strip()
    if not query:
        return jsonify({'error': 'No query provided'}), 400
    
    start = int(request.args.get('start', 0))
    results = search_engine.search(query, start=start)
    
    return jsonify(results)

@app.route('/health')
def health():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'timestamp': datetime.utcnow().isoformat(),
        'version': '2.0.0'
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=os.getenv('DEBUG', 'false').lower() == 'true')
