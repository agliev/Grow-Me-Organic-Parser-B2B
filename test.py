import requests

HEADERS = {"Cookie": '_gcl_au=1.1.1018492616.1654861675; tk_or=%22https%3A%2F%2Fwww.google.com%2F%22; _fbp=fb.1.1654861680272.1737963368; _hjSessionUser_2739501=eyJpZCI6IjYyY2QzNDU0LTk4ZWMtNTBiYi1iMWJjLWQwMjNkYTM0ZTRlZiIsImNyZWF0ZWQiOjE2NTQ4NjE2ODA1NDQsImV4aXN0aW5nIjp0cnVlfQ==; usetiful-visitor-ident=a8f91f19-1fa3-4ac8-31aa-1708dae1bb09; crisp-client%2Fsession%2F2dc87a17-fcbe-4c6b-ac38-cbd56e9e2376=session_b17d699e-12b9-4efa-8bc5-d18afb10ef1f; crisp-client%2Fsocket%2F2dc87a17-fcbe-4c6b-ac38-cbd56e9e2376=1; _tcfpup=1657190242155; ti_ukp=88464a3d.db6d.32db.0076.2f019bfe974e; _oauth_id_token_cookie_sub=628a43323f3cf5bd228b7d2d; _gid=GA1.2.244785558.1657454838; tk_r3d=%22https%3A%2F%2Fwww.google.com%2F%22; _oauth_id_token_cookie=6d4ab3444a4ceedc08593e7827f62d63-4e3b440afed7182eebd965d6404a2df7-c208fcf8fcb045cc838398bb6eaa4c8b-fa929a210d3c145de9844fffa159a221; tk_lr=%22%22; _hjSession_2739501=eyJpZCI6IjE0YzkzZDE5LTgxODAtNDIzNy1iYTA4LTM0NWM0OWJlNzViMiIsImNyZWF0ZWQiOjE2NTc3MTU3OTIzMTIsImluU2FtcGxlIjpmYWxzZX0=; _hjAbsoluteSessionInProgress=0; _ga=GA1.2.2136330129.1654861678; _tcSessInfo={"timestamp":1657718049930,"pageView":0}; _tcSecSess={"sess":"d48167b99e82f5ee8b0fa473136","device_type":"desktop","ip":"45.14.71.x","tcvfp":"baad5b2b-e6de-adf2-3460-9da708465157","locale":"ru_RU","country":"NL","city":"","region":"","timestamp":1657718053032}; _tcafterScoket=1; PHPSESSID=at7326eq3arro2n96deqm84et4; _oauth_id_token=KVS_SUB628a43323f3cf5bd228b7d2d; _ga_E61RPSQPM7=GS1.1.1657718048.18.1.1657718069.0'}


file_url = requests.get('https://apps.growmeorganic.com/api-product/load-companies-tasks-exported', 
                                                                             headers=HEADERS).json()
u = [url['file_url'] for url in file_url['data']]

print(f"inductry - {u[1].split('-')[9]}, country - {u[1].split('-')[8]}")
print(u[1])

