from pydantic import BaseModel

from fastapi import APIRouter, status, Depends, HTTPException
from fastapi.responses import FileResponse

import uuid

from typing import Annotated

from selenium import webdriver

from selenium.webdriver.common.by import By

import datetime
