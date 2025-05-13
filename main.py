import os
import requests
import socket

def get_ip_list(url):
    response = requests.get(url)
    response.raise_for_status()
    raw_ips = response.text.strip().split('\n')
    ip_list = list(set(ip.strip() for ip in raw_ips if ip.strip()))
    return ip_list

def is_ip_reachable(ip, ports=(80, 443), timeout=5):
    for port in ports:
        try:
            with socket.create_connection((ip, port), timeout=timeout):
                return True
        except Exception:
            continue
    return False

def filter_usable_ips(ip_list):
    unique_ips = list(set(ip_list))
    return [ip for ip in unique_ips if is_ip_reachable(ip)]

def get_cloudflare_zone(api_token):
    headers = {
        'Authorization': f'Bearer {api_token}',
        'Content-Type': 'application/json',
    }
    response = requests.get('https://api.cloudflare.com/client/v4/zones', headers=headers)
    response.raise_for_status()
    zones = response.json().get('result', [])
    if not zones:
        raise Exception("No zones found")
    return zones[0]['id'], zones[0]['name']

def delete_existing_dns_records(api_token, zone_id, subdomain, domain):
    headers = {
        'Authorization': f'Bearer {api_token}',
        'Content-Type': 'application/json',
    }
    record_name = domain if subdomain == '@' else f'{subdomain}.{domain}'
    while True:
        response = requests.get(f'https://api.cloudflare.com/client/v4/zones/{zone_id}/dns_records?type=A&name={record_name}', headers=headers)
        response.raise_for_status()
        records = response.json().get('result', [])
        if not records:
            break
        for record in records:
            delete_response = requests.delete(f'https://api.cloudflare.com/client/v4/zones/{zone_id}/dns_records/{record["id"]}', headers=headers)
            delete_response.raise_for_status()
            print(f"删除记录 {subdomain}: {record['id']}")

def update_cloudflare_dns(ip_list, api_token, zone_id, subdomain, domain):
    headers = {
        'Authorization': f'Bearer {api_token}',
        'Content-Type': 'application/json',
    }
    record_name = domain if subdomain == '@' else f'{subdomain}.{domain}'
    for ip in ip_list:
        data = {
            "type": "A",
            "name": record_name,
            "content": ip,
            "ttl": 1,
            "proxied": False
        }
        response = requests.post(f'https://api.cloudflare.com/client/v4/zones/{zone_id}/dns_records', json=data, headers=headers)
        if response.status_code == 200:
            print(f"添加记录 {subdomain}: {ip}")
        else:
            print(f"添加失败 {ip} 到 {subdomain}: {response.status_code} {response.text}")

if __name__ == "__main__":
    api_token = os.getenv('CF_API_TOKEN')
    
    subdomain_ip_mapping = {
        'bestcf': 'https://raw.githubusercontent.com/ohtonarmoht/youxuanyuming/refs/heads/main/ip_raw.txt',
    }

    try:
        zone_id, domain = get_cloudflare_zone(api_token)

        for subdomain, url in subdomain_ip_mapping.items():
            raw_ips = get_ip_list(url)
            print(f"获取到 {len(raw_ips)} 个原始 IP，正在测试可用性...")
            usable_ips = filter_usable_ips(raw_ips)
            print(f"通过测试的 IP 有 {len(usable_ips)} 个，开始更新 DNS")
            delete_existing_dns_records(api_token, zone_id, subdomain, domain)
            update_cloudflare_dns(usable_ips, api_token, zone_id, subdomain, domain)

    except Exception as e:
        print(f"发生错误: {e}")
