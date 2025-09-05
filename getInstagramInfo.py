import requests
import json

# Use your existing token first, then new one if needed
LONG_TOKEN = "token here"

def test_connection():
    """Test if Instagram Business account is now connected"""
    
    print("=== Testing Instagram Business Connection ===")
    
    # Step 1: Check if Facebook pages now show Instagram connection
    pages_url = "https://graph.facebook.com/me/accounts"
    pages_params = {
        "fields": "name,instagram_business_account{id,username,followers_count,media_count}",
        "access_token": LONG_TOKEN
    }
    
    try:
        pages_response = requests.get(pages_url, params=pages_params)
        pages_data = pages_response.json()
        
        print("Facebook Pages Response:")
        print(json.dumps(pages_data, indent=2))
        
        # Check if we found Instagram connection
        if 'data' in pages_data and len(pages_data['data']) > 0:
            for page in pages_data['data']:
                if 'instagram_business_account' in page:
                    instagram_account = page['instagram_business_account']
                    print(f"\n✅ Found Instagram Business Account!")
                    print(f"Instagram ID: {instagram_account['id']}")
                    print(f"Username: @{instagram_account['username']}")
                    
                    # Test getting media from this account
                    return test_instagram_media(instagram_account['id'])
            
            print("❌ No Instagram business accounts found in Facebook pages")
            return False
        else:
            print("❌ No Facebook pages found or permission issue")
            return False
            
    except Exception as e:
        print(f"Error testing connection: {e}")
        return False

def test_instagram_media(instagram_id):
    """Test getting Instagram media and insights"""
    
    print(f"\n=== Testing Instagram Media for ID: {instagram_id} ===")
    
    # Get basic account info
    account_url = f"https://graph.facebook.com/{instagram_id}"
    account_params = {
        "fields": "id,username,followers_count,follows_count,media_count,profile_picture_url",
        "access_token": LONG_TOKEN
    }
    
    try:
        account_response = requests.get(account_url, params=account_params)
        account_data = account_response.json()
        
        if 'error' in account_data:
            print(f"❌ Account info error: {account_data['error']['message']}")
            return False
            
        print("✅ Account Info:")
        print(json.dumps(account_data, indent=2))
        
        # Get recent media
        media_url = f"https://graph.facebook.com/{instagram_id}/media"
        media_params = {
            "fields": "id,caption,media_type,media_url,permalink,timestamp,like_count,comments_count",
            "access_token": LONG_TOKEN,
            "limit": 5
        }
        
        media_response = requests.get(media_url, params=media_params)
        media_data = media_response.json()
        
        if 'error' in media_data:
            print(f"❌ Media error: {media_data['error']['message']}")
            return False
            
        print("\n✅ Recent Media:")
        print(json.dumps(media_data, indent=2))
        
        # Test insights (analytics)
        if 'data' in media_data and len(media_data['data']) > 0:
            test_media_insights(media_data['data'][0]['id'])
        
        return True
        
    except Exception as e:
        print(f"Error testing media: {e}")
        return False

def test_media_insights(media_id):
    """Test getting insights for a specific post"""
    
    print(f"\n=== Testing Insights for Media: {media_id} ===")
    
    insights_url = f"https://graph.facebook.com/{media_id}/insights"
    insights_params = {
        "metric": "impressions,reach,engagement",
        "access_token": LONG_TOKEN
    }
    
    try:
        insights_response = requests.get(insights_url, params=insights_params)
        insights_data = insights_response.json()
        
        if 'error' in insights_data:
            print(f"❌ Insights error: {insights_data['error']['message']}")
            print("Note: Insights require instagram_manage_insights permission")
        else:
            print("✅ Media Insights:")
            print(json.dumps(insights_data, indent=2))
            
    except Exception as e:
        print(f"Error testing insights: {e}")

def check_token_info():
    """Debug token information"""
    print("=== Token Information ===")
    print(f"Token length: {len(LONG_TOKEN)}")
    print(f"Token starts with: {LONG_TOKEN[:30]}...")
    print(f"Token ends with: ...{LONG_TOKEN[-10:]}")

# Run all tests
if __name__ == "__main__":
    check_token_info()
    
    if test_connection():
        print("\n🎉 SUCCESS! Your Instagram Business account is connected!")
        print("You can now build your analytics dashboard!")
    else:
        print("\n❌ Connection failed. Check:")
        print("1. Instagram is connected to a Facebook Page")
        print("2. Token has instagram_basic and pages_show_list permissions")
        print("3. You're added as an Instagram Tester in the app")
        print("4. Try generating a new token with updated permissions")