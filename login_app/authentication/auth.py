from typing import Optional
from fastapi.security import OAuth2PasswordBearer
from jose import jwt
from datetime import datetime,timezone,timedelta


oauth2_scheme=OAuth2PasswordBearer(tokenUrl='token')


SECRET_KEY='ce8ae10de3a56d67cbc1de8eb53c787ad9444ae628a342fa1543bf8923d3b0e6'
ALGORITHM='HS256'
ACCESS_TOKEN_EXPIRE_MINNUTES=20

def create_access_token(data:dict,expire_time:Optional[timedelta]=None):
    to_encode=data.copy()
    expire = datetime.now(timezone.utc)+(expire_time if expire_time else timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINNUTES))
    to_encode.update({'exp':expire})
    encoded_jwt=jwt.encode(to_encode,SECRET_KEY,algorithm=ALGORITHM)
    return encoded_jwt        