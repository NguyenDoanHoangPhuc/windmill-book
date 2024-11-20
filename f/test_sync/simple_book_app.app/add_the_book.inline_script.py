import os
import wmill

from supabase import Client, create_client

def main(
    id: str,
    tittle: str,
    authors: str,
    description: str,
    imageLinks: str    
):
    key = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InBndHF4d2t0ZGxidmxpeGxvYmlzIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MzEzMzM0NjYsImV4cCI6MjA0NjkwOTQ2Nn0.Yah1ejtu35u0N-17ZsjBYV2fYNJ4nNvlGsU5T-gpfek'
    url = 'https://pgtqxwktdlbvlixlobis.supabase.co'
    supabase: Client = create_client(url, key)

    data = {
        'id': id,
        'title': tittle,
        'authors': authors,
        'description': description,
        'imagelinks': imageLinks
    }

    response = (
    supabase.table("book")
    .insert(data)
    .execute())

    return response


    