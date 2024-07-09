import requests

def get_ip_location(ip):
    try:
        response = requests.get(f'http://ipapi.co/{ip}/json/')
        if response.status_code == 200:
            data = response.json()
            return {
                'IP': ip,
                'City': data.get('city', 'N/A'),
                'Region': data.get('region', 'N/A'),
                'Country': data.get('country_name', 'N/A'),
                'Latitude': data.get('latitude', 'N/A'),
                'Longitude': data.get('longitude', 'N/A')
            }
        else:
            return {'error': f'Error: {response.status_code}'}
    except Exception as e:
        return {'error': str(e)}

if __name__ == '__main__':
    ip = input("Enter the IP address: ")
    location = get_ip_location(ip)
    print(location)
