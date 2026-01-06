from enum import Enum
from typing import List, Optional

class Role(Enum):
    FEDEX_ADMIN = "FEDEX_ADMIN"
    DCA_AGENT = "DCA_AGENT"

class Case:
    def __init__(self, case_id, dca_id, debt_amount):
        self.case_id = case_id
        self.dca_id = dca_id
        self.debt_amount = debt_amount

# Mock Database
all_cases = [
    Case(101, "AGENCY_A", 5000),
    Case(102, "AGENCY_B", 3000),
    Case(103, "AGENCY_A", 1500)
]

def get_cases(user_role: Role, user_dca_id: Optional[str] = None):
    """
    Enforces secure case allocation and tracking 
    """
    if user_role == Role.FEDEX_ADMIN:
        # Admins have full visibility for analytics and insights [cite: 17, 23]
        return all_cases
    
    if user_role == Role.DCA_AGENT:
        # DCAs only see their specific assigned accounts 
        return [c for c in all_cases if c.dca_id == user_dca_id]
    
    return []
