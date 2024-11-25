from supabase import create_client, Client


def main(
    url: str,
    key: str,
    account_id: int
):
   
    supabase: Client = create_client(url, key)
    
    response = supabase.table("accounts").select("*").eq("id", account_id).execute()
    print(response.data[0])
