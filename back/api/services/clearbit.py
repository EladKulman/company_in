import aiohttp
import asyncio


URL = 'https://company.clearbit.com/v2/companies/find?domain={}'

async def get_company_data(domain):
    headers ={'Authorization': 'Bearer sk_30240e2d1dfc1d73d26ab80390d1fd49' }
    url = URL.format(domain)
    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=headers) as response:
            response = await response.json()
            if 'error' in response:
                message = response['error']['message']
                return {'success': False, 'data': {'message': message}}
            return {'success': True, 'data': response}
            




# loop = asyncio.get_event_loop()
# loop.run_until_complete(get_company_data('google.com'))