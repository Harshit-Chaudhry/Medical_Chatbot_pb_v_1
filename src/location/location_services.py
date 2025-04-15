import googlemaps
import os
from dotenv import load_dotenv
from datetime import datetime, timedelta
import json

class LocationServices:
    def __init__(self):
        load_dotenv()
        self.api_key = os.getenv('GOOGLE_MAPS_API_KEY')
        self.client = googlemaps.Client(key=self.api_key)
    
    def find_nearby_healthcare(self, location, radius=5000, type='hospital'):
        """Find nearby healthcare facilities"""
        try:
            
            geocode_result = self.client.geocode(location)
            if not geocode_result:
                return "Location not found. Please try again with a more specific address."
            
            
            lat = geocode_result[0]['geometry']['location']['lat']
            lng = geocode_result[0]['geometry']['location']['lng']
            
            
            places_result = self.client.places_nearby(
                location=(lat, lng),
                radius=radius,
                type=type,
                keyword='healthcare'
            )
            
            
            results = []
            for place in places_result.get('results', []):
                
                place_details = self.client.place(
                    place['place_id'],
                    fields=['name', 'formatted_address', 'rating', 'opening_hours', 'website', 'formatted_phone_number']
                )['result']
                
                result = {
                    'name': place_details.get('name'),
                    'address': place_details.get('formatted_address'),
                    'rating': place_details.get('rating'),
                    'phone': place_details.get('formatted_phone_number'),
                    'website': place_details.get('website'),
                    'opening_hours': place_details.get('opening_hours', {}).get('weekday_text', [])
                }
                results.append(result)
            
            return results
        
        except Exception as e:
            return f"Error finding healthcare facilities: {str(e)}"
    
    def get_directions(self, origin, destination):
        """Get directions between two locations"""
        try:
            directions = self.client.directions(
                origin,
                destination,
                mode="driving",
                departure_time=datetime.now()
            )
            
            if not directions:
                return "No directions found."
            
            
            route = directions[0]
            steps = []
            
            for leg in route['legs']:
                for step in leg['steps']:
                    steps.append({
                        'instruction': step['html_instructions'],
                        'distance': step['distance']['text'],
                        'duration': step['duration']['text']
                    })
            
            return {
                'total_distance': route['legs'][0]['distance']['text'],
                'total_duration': route['legs'][0]['duration']['text'],
                'steps': steps
            }
        
        except Exception as e:
            return f"Error getting directions: {str(e)}"
    
    def save_appointment(self, appointment_data):
        """Save appointment details to file"""
        try:
            
            os.makedirs('data/appointments', exist_ok=True)
            
            
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            filename = f'data/appointments/appointment_{timestamp}.json'
            
            
            with open(filename, 'w') as f:
                json.dump(appointment_data, f, indent=4)
            
            return f"Appointment saved successfully: {filename}"
        
        except Exception as e:
            return f"Error saving appointment: {str(e)}" 