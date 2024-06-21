import requests
from urllib.parse import urlparse, parse_qs

def extract_contest_slug(contest_link):
    parsed_url = urlparse(contest_link)
    path_components = parsed_url.path.split('/')
    
    if 'contest' in path_components:
        contest_slug_index = path_components.index('contest') + 1
        if contest_slug_index < len(path_components):
            return path_components[contest_slug_index]
    
    return None

def construct_leaderboard_url(contest_slug, page_num):
    if not contest_slug:
        raise ValueError("Contest slug cannot be None.")
    
    # Construct leaderboard API URL
    url = f"https://practiceapi.geeksforgeeks.org/api/latest/contest/{contest_slug}/leaderboard/?page={page_num}"
    return url

def find_handle_page(handle_to_find, total_pages, contest_link, cookies):
    session = requests.Session()
    session.headers.update({
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
        'Cookie': cookies
    })

    contest_slug = extract_contest_slug(contest_link)
    if not contest_slug:
        print(f"Invalid contest link: {contest_link}")
        return None

    handle_found = False

    for page_num in range(1, total_pages + 1):
        if handle_found:
            break
        
        url = construct_leaderboard_url(contest_slug, page_num)
        
        try:
            response = session.get(url)
            response.raise_for_status()
            leaderboard_data = response.json()
            
            ranks_list = leaderboard_data.get('results', {}).get('ranks_list', [])
            
            for entry in ranks_list:
                if entry.get('handle') == handle_to_find:
                    print(f"Handle '{handle_to_find}' found on page {page_num}.")
                    print("Details:")
                    print(f"  last_correct_submission: {entry.get('last_correct_submission')}")
                    print(f"  coding_score: {entry.get('coding_score')}")
                    print(f"  user_id: {entry.get('user_id')}")
                    print(f"  handle: {entry.get('handle')}")
                    print(f"  has_plagiarism_submissions_for_user: {entry.get('has_plagiarism_submissions_for_user')}")
                    print(f"  profile_link: {entry.get('profile_link')}")
                    print(f"  rank: {entry.get('rank')}")
                    print(f"  score: {entry.get('score')}")
                    print(f"  time_penalty_txt: {entry.get('time_penalty_txt')}")
                    handle_found = True
                    break
            
            if not handle_found:
                print(f"Handle '{handle_to_find}' not found on page {page_num}.")
        
        except requests.exceptions.RequestException as e:
            print(f"Failed to fetch page {page_num}. Error: {e}")
    
    return page_num if handle_found else None

# Example usage
def main():
    contest_link = input("Enter the contest link: ").strip()
    handle_to_find = input("Enter the handle name: ").strip()
    total_pages = int(input("Enter the total pages in leaderboard: ").strip())
    
    # Paste your captured Cookie header value here accordingly ( use GPT to order it )
    cookies = (
        "gfg_id5_identity=<gfg_id5_identity_value>; "
        "csrftoken=<csrftoken_value>; "
        "gfg_nluid=<gfg_nluid_value>; "
        "g_state=<g_state_value>; "
        "gfg_ugen=<gfg_ugen_value>; "
        "gfg_utype=<gfg_utype_value>; "
        "gfg_ugy=<gfg_ugy_value>; "
        "gfg_uspl_1=<gfg_uspl_1_value>; "
        "gfg_uspl_2=<gfg_uspl_2_value>; "
        "gfg_uspl_3=<gfg_uspl_3_value>; "
        "geeksforgeeks_consent_status=<geeksforgeeks_consent_status_value>; "
        "CloudFront-Key-Pair-Id=<CloudFront-Key-Pair-Id_value>; "
        "authtoken=<authtoken_value>; "
        "gfguserName=<gfguserName_value>; "
        "gfgpromoparams=<gfgpromoparams_value>; "
        "http_referrer=<http_referrer_value>; "
        "ext_name=<ext_name_value>; "
        "gfg_theme=<gfg_theme_value>; "
        "CloudFront-Policy=<CloudFront-Policy_value>; "
        "CloudFront-Signature=<CloudFront-Signature_value>; "
    )


    page_number = find_handle_page(handle_to_find, total_pages, contest_link, cookies)

    if page_number:
        print(f"Handle '{handle_to_find}' found on page {page_number-1}.")
    else:
        print(f"Handle '{handle_to_find}' not found on any page.")

if __name__ == "__main__":
    main()
