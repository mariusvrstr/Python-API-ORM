from src.data_access.clients.common.client_base import ClientBase

class CompanyClient(ClientBase):

    def __init__(self) -> None:
        super().__init__('https://api.inoxico-uat.com/api/company/v1')
        self.add_header('Content-Type', 'application/json')
        self.add_header('Host', 'api.inoxico-uat.com')
        self.add_basic_auth('user@inoxico.com','*****')

    def get_company_by_noxid(self, noxid):

        json_request = {
            "noxId": noxid,
            "allModules": True
        }

        response = self.set_payload(json_request).post('getCompany')
        return response
