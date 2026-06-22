from supabase import create_client, Client

from src.config import (
    SUPABASE_URL,
    SUPABASE_KEY
)

class SupabaseClient:
    
    def __init__(self):
        self.client: Client = create_client(
            SUPABASE_URL,
            SUPABASE_KEY
        )
        
    def get_contacts(self, limit: int = 3):
        """
        Busca até 3 contatos;
        
        """
        response = (
            self.client
            .table("contatos")
            .select("*")
            .limit(limit)
            .execute()
        )
        
        return response.data
        