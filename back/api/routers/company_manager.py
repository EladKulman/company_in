from fastapi import APIRouter, Request, Depends, Response, encoders, HTTPException
from pydantic import BaseModel
from api import config
from api.model.companies_model import add_company, get_all_companies_summary,get_company_details
import json
import aiohttp 
from api.services import clearbit
from pprint import pprint



companies_router = r = APIRouter()

class NewCompanyModel(BaseModel):
    domain: str
   

@r.get("/summary/all")
async def get_companies_summary():
    return get_all_companies_summary()


@r.get("/details/{company_name}")
async def get_companies_summary(company_name: str):
    company_details, err = get_company_details(company_name) 
    if err:
        raise HTTPException(status_code=404, detail=err)
    return company_details



@r.post("/")
async def add_new_company(payload: NewCompanyModel):
    response = await clearbit.get_company_data(payload.domain)
    if response['success']:
        company_data = response['data']
        success, err =  add_company(company_data)
        if err:
            raise HTTPException(status_code=409, detail=err)
        company_sum = {'name' : company_data['name'], 'logo' : company_data['logo'], 'type': company_data['type']}
        return company_sum
    else:
        raise HTTPException(status_code=404, detail=company_data['message'])
   





# async def fetch_asynchronous(cls, url: str, n: int = 100) -> dict:
#     """[summary]

#     Args:
#         url (str): [description]
#         n (int): [description]

#     Returns:
#         dict: [description]
#     """ 
#     try:
#         result = {'data':[]}
#         async with aiohttp.ClientSession() as session:
#             responses = await asyncio.gather(*[session.get(url, ssl=False) for _ in range(n)])
#             # print(responses)
#             # print("***")
#             for response in responses:
#                 result['data'].append(await response.json())

#         result['success'] = True
#         return result 
#     except Exception as e:
#         print(f"error {e}")
#         traceback.print_exc()
#         return {'success': False, 'detail':str(e)}          

# @r.post("/users", response_model=User, response_model_exclude_none=True)
# async def user_create(
#     request: Request,
#     user: UserCreate,
#     db=Depends(get_db),
#     # current_user=Depends(get_current_active_superuser),
# ):
#     """
#     Create a new user
#     """
#     result = create_user(db, user)
#     celery_worker.send_task('new_user_task.process_new_user', kwargs={'id': result.id})
#     return result