import requests
import urllib3
import getpass

urllib3.disable_warnings()


def auth_session(url):
    user = str(input("Provide the vCenter Username: "))
    print(user)
    # password = getpass.getpass(prompt="Provide the Password: ", stream=None)
    vcenter_auth_url = f'{url}/rest/com/vmware/cis/session'
    print(vcenter_auth_url)
    # vcenter_url = "https://10.10.10.11/api/vcenter"
    auth_r = requests.post(f'{vcenter_auth_url}', auth=(user, getpass.getpass()), verify=False)
    kuki = auth_r.text["value"]

auth_session("https://10.10.10.11")
print(auth_session.kuki)

# payload = {
#     "vmware-api-session-id": auth_r_json["value"]
# }

# json_r = requests.get(f'{vcenter_url}/vm', cookies=auth_r.cookies, verify=False)
# print(json_r.status_code)
# print(json_r.json())
