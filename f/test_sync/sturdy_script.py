import os
import wmill
from supabase import Client, create_client


def main(
    
):
    key = wmill.get_variable("u/hoangphuc090104/supabase_anon_key")
    url = wmill.get_variable("u/hoangphuc090104/supabase_url")
    supabase: Client = create_client(url, key)
    response = supabase.table("book").select("*").execute()
    return response.data

    