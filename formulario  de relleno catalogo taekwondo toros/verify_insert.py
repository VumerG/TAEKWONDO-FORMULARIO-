import json
import urllib.request

SUPABASE_URL = 'https://kayjrplfpvxcqynznnwn.supabase.co'
ANON_KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImtheWpycGxmcHZ4Y3F5bnpubnduIiwicm9sZSI6ImFub24iLCJpYXQiOjE3ODExMTYzNDYsImV4cCI6MjA5NjY5MjM0Nn0.yJgdL-_BJymfqU4iGoeNN-X826TcMJMDhyu4MUTYqIg'
SERVICE_ROLE = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImtheWpycGxmcHZ4Y3F5bnpubnduIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTc4MTExNjM0NiwiZXhwIjoyMDk2NjkyMzQ2fQ.uBMPG4wV4ngg7CaBRao14Tx8TNpi74JeZwBPJ_Pldc8'

payload = {
    'nombre_producto': 'Verificacion CLI',
    'codigo': 'CLI-TEST',
    'categoria': 'Test',
    'precio': 9.99,
    'stock': 1,
    'estado': 'Disponible'
}

req = urllib.request.Request(
    f'{SUPABASE_URL}/rest/v1/products',
    data=json.dumps(payload).encode('utf-8'),
    headers={
        'Content-Type': 'application/json',
        'apikey': ANON_KEY,
        'Authorization': f'Bearer {SERVICE_ROLE}',
        'Prefer': 'return=representation'
    },
    method='POST'
)

with urllib.request.urlopen(req) as resp:
    print('POST_STATUS', resp.status)
    print('POST_BODY', resp.read().decode('utf-8'))
