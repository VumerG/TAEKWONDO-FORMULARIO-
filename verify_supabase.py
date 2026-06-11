import json
import urllib.request

SUPABASE_URL = 'https://kayjrplfpvxcqynznnwn.supabase.co'
ANON_KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImtheWpycGxmcHZ4Y3F5bnpubnduIiwicm9sZSI6ImFub24iLCJpYXQiOjE3ODExMTYzNDYsImV4cCI6MjA5NjY5MjM0Nn0.yJgdL-_BJymfqU4iGoeNN-X826TcMJMDhyu4MUTYqIg'
SERVICE_ROLE = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImtheWpycGxmcHZ4Y3F5bnpubnduIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTc4MTExNjM0NiwiZXhwIjoyMDk2NjkyMzQ2fQ.uBMPG4wV4ngg7CaBRao14Tx8TNpi74JeZwBPJ_Pldc8'

url = f'{SUPABASE_URL}/rest/v1/products?select=*&limit=1'
req = urllib.request.Request(url, headers={
    'apikey': ANON_KEY,
    'Authorization': f'Bearer {SERVICE_ROLE}',
})

try:
    with urllib.request.urlopen(req) as resp:
        print('STATUS', resp.status)
        print('BODY', resp.read().decode('utf-8'))
except Exception as exc:
    import traceback
    print('ERROR_CLASS', type(exc).__name__)
    if hasattr(exc, 'code'):
        print('ERROR_CODE', exc.code)
    if hasattr(exc, 'read'):
        try:
            print('ERROR_BODY', exc.read().decode('utf-8'))
        except Exception:
            pass
    traceback.print_exc()
