from fastapi import HTTPException

def raise_not_found(message: str = "Item not found"):
    raise HTTPException(status_code=404, detail=message)

def raise_server_error(message: str = "Internal server error"):
    raise HTTPException(status_code=500, detail=message)
