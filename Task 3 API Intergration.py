"""
Codveda Internship — Level 2, Task 3: API Integration
Author: Clemence"""



import requests

def get_zim_market_rates():
    print("--- Zimbabwe Financial Market Rates ---")
    
    # Using an open API to fetch global exchange rates relative to USD
    url = "https://open.er-api.com/v6/latest/USD"
    
    try:
        response = requests.get(url)
        
        if response.status_code == 200:
            data = response.json()
            rates = data.get("rates", {})
            
            # Fetching regional currencies for comparison (ZWG, ZAR, BWP)
            
            zwg_rate = rates.get("ZWG")
            zar_rate = rates.get("ZAR")
            bwp_rate = rates.get("BWP")
            
            print("\n======================================")
            print(" Official Exchange Rates (Base: 1 USD)")
            print("======================================")
            
            if zwg_rate:
                print(f"USD to ZWG (Zimbabwe Gold) : {zwg_rate:.4f}")
            else:
                # Fallback display if the specific API index is updating
                print("USD to ZWG (Zimbabwe Gold) : Rate temporarily unavailable on this feed")
                
            print(f"USD to ZAR (South African Rand): {zar_rate:.4f}" if zar_rate else "ZAR Rate unavailable")
            print(f"USD to BWP (Botswana Pula)     : {bwp_rate:.4f}" if bwp_rate else "BWP Rate unavailable")
            print("======================================")
            print(f"Last Updated by Provider       : {data.get('time_last_update_utc', 'Unknown')}")
            print("======================================")
            
        else:
            print(f"Failed to fetch rates. Status Code: {response.status_code}")
            
    except requests.exceptions.ConnectionError:
        print("Network Error: Could not connect to the server. Please check your internet connection.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Run the local rate fetcher
get_zim_market_rates()
