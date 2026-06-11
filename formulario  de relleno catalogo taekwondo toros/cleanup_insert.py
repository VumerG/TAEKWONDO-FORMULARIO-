import urllib.request

SUPABASE_URL = 'https://kayjrplfpvxcqynznnwn.supabase.co'
ANON_KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImtheWpycGxmcHZ4Y3F5bnpubnduIiwicm9sZSI6ImFub24iLCJpYXQiOjE3ODExMTYzNDYsImV4cCI6MjA5NjY5MjM0Nn0.yJgdL-_BJymfqU4iGoeNN-X826TcMJMDhyu4MUTYqIg'
SERVICE_ROLE = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImtheWpycGxmcHZ4Y3F5bnpubnduIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTc4MTExNjM0NiwiZXhwIjoyMDk2NjkyMzQ2fQ.uBMPG4wV4ngg7CaBRao14Tx8TNpi74JeZwBPJ_Pldc8'

req = urllib.request.Request(
    f'{SUPABASE_URL}/rest/v1/products?codigo=eq.CLI-TEST',
    headers={
        'apikey': ANON_KEY,
        'Authorization': f'Bearer {SERVICE_ROLE}',
    },
    method='DELETE'
)

with urllib.request.urlopen(req) as resp:
    print('DELETE_STATUS', resp.status)
    print('DELETE_BODY', resp.read().decode('utf-8'))
