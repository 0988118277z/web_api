from pydantic import BaseModel, validator, Field
from fastapi import APIRouter, Request, Depends
from ipaddress import ip_network, IPv4Address#(不含子遮)
from moduley.geoipy import iplookup
from sqly import schemas

router = APIRouter(
    prefix="/api/v1/ipv4",
    tags=["IPv4"],
)

class IPcheck(BaseModel):
    address: str = Field(..., example="1.2.3.4/5")
    # strict: bool = False  #true=不含子遮, false=含子遮

    @validator('address')
    def validate_ipv4_network(cls, v, values):
        strict_mode = values.get('strict', False)
        try:
            return str(ip_network(v, strict=strict_mode))
        except ValueError as e:
            raise ValueError(f"{v} does not appear to be an IPv4 network")

@router.get("/ip-getinfo")
async def get_ip_info(ipaddress: schemas.AddressV4 = Depends()):
    # client_host = request.client.host
    # client_port = request.client.port   
    if ipaddress.iip:
        return await iplookup(ipaddress.iip)
    else:
        return f"input does not appear to be an IPv4 network"

@router.get("/ip-myinfo")
async def request_ip_info(request: Request):
    try:
        return await iplookup(request.client.host)
    except:
        return f'{request.client.host} is not public'
    
@router.post("/ip-compute")
async def compute_ip(ip: IPcheck):
    submask_list = {'0':256,'1':128,'2':64,'3':32,'4':16,'5':8,'6':4,'7':2}
    
    ipaddr = [ int(i) for i in str(ip.address).split('/')[0].split('.') ]  #取得IP
    submask = int(str(ip.address).split('/')[1])  #取得子遮

    temp_num1 = submask // 8  #選擇要處理的範圍
    temp_num2 = str(submask % 8)  #網段IP數量

    ip_address = {'ip_address':f'{ipaddr[0]}.{ipaddr[1]}.{ipaddr[2]}.{ipaddr[3]}' }
    if submask == 32:
        ip_address['network_name'] = ip_address['ip_address']
        ip_address['broadcast'] = ip_address['ip_address']
        ip_address['available_ip_range'] = ip_address['ip_address']
        ip_address['available_ip_amount'] = 1
        return ip_address

    for i in range(256//submask_list[temp_num2]):
        if (submask_list[temp_num2]*i) <= ipaddr[temp_num1] and (ipaddr[temp_num1] <= (submask_list[temp_num2]*(i+1)-1)):
            networkname = submask_list[temp_num2]*i
            broadcast = submask_list[temp_num2]*(i+1)-1
            
            if temp_num1 == 0:
                network_ip = f'{networkname}.0.0.0'
                boradcast_ip = f'{broadcast}.255.255.255'
                ip_address['network_name'] = network_ip
                ip_address['broadcast'] = boradcast_ip
                ip_address['available_ip_range'] = f'{networkname}.0.0.1 ~ {broadcast}.255.255.254'
                ip_address['available_ip_amount'] = (broadcast-networkname+1)*256*256*256-2
                
            elif temp_num1 == 1:
                network_ip = f'{ipaddr[0]}.{networkname}.0.0'
                boradcast_ip = f'{ipaddr[0]}.{broadcast}.255.255'
                ip_address['network_name'] = network_ip
                ip_address['broadcast'] = boradcast_ip
                ip_address['available_ip_range'] = f'{ipaddr[0]}.{networkname}.0.1 ~ {ipaddr[0]}.{broadcast}.255.254'
                ip_address['available_ip_amount'] = (broadcast-networkname+1)*256*256-2

            elif temp_num1 == 2:
                network_ip = f'{ipaddr[0]}.{ipaddr[1]}.{networkname}.0'
                boradcast_ip = f'{ipaddr[0]}.{ipaddr[1]}.{broadcast}.255'
                ip_address['network_name'] = network_ip
                ip_address['broadcast'] = boradcast_ip
                ip_address['available_ip_range'] = f'{ipaddr[0]}.{ipaddr[1]}.{networkname}.1 ~ {ipaddr[0]}.{ipaddr[1]}.{broadcast}.254'
                ip_address['available_ip_amount'] = (broadcast-networkname+1)*256-2

            elif temp_num1 == 3:
                network_ip = f'{ipaddr[0]}.{ipaddr[1]}.{ipaddr[2]}.{networkname}'
                boradcast_ip = f'{ipaddr[0]}.{ipaddr[1]}.{ipaddr[2]}.{broadcast}'
                ip_address['network_name'] = network_ip
                ip_address['broadcast'] = boradcast_ip
                ip_address['available_ip_range'] = f'{ipaddr[0]}.{ipaddr[1]}.{ipaddr[2]}.{networkname + 1} ~ {ipaddr[0]}.{ipaddr[1]}.{ipaddr[2]}.{broadcast -1}'
                ip_address['available_ip_amount'] = (broadcast-networkname+1)-2
        
    return ip_address


# 在 FastAPI 中，Request 物件來自 Starlette 框架，包含了許多屬性和方法，使得你能夠訪問和處理 HTTP 請求的各種數據。以下是一些你可以從 Request 物件中訪問的重要屬性和方法：

# 屬性
# method: 字符串，顯示 HTTP 請求方法（如 GET, POST, PUT 等）。
# url: 包含完整請求 URL 的 URL 對象。
# headers: 包含請求標頭的不可變多字典（MultiDict）。
# query_params: 包含 URL 查詢參數的不可變多字典。
# path_params: 包含路徑參數的字典（例如在路由中定義的 "/items/{item_id}" 中的 item_id）。
# client: 包含客戶端連接信息的元組，如前述 host 和 port。
# cookies: 包含所有 cookies 的字典。
# state: 可以用來存儲請求期間的數據，這在處理請求時非常有用。
# app: 指向創建該請求的 FastAPI 應用。