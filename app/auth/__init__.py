from datetime import datetime, timedelta, timezone
from pydantic import BaseModel
from fastapi.security import HTTPBearer
from fastapi import Depends, HTTPException, status
from typing import Annotated
from jwt.exceptions import InvalidTokenError