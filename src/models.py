import requests
import pandas as pd


class GrowMeOrganic:
    def __init__(self, headers: dict = None):
        self.headers = headers

    def _update_headers():
        pass

    def get_task(self, country: str, industry: str, size: str) -> int:
        response = requests.get(
            "https://apps.growmeorganic.com/api-product/load-companies-tasks-exported",
            headers=self.headers,
        ).json()["data"]

        filtered = list(
            filter(
                lambda x: x["country"] == country
                and x["industry"] == industry
                and x["size"] == size,
                response,
            )
        )

        if len(filtered) > 0:
            return True
        elif len(filtered) == 0:
            return False

    def trigger_report(self, country: str, industry: str, size: str) -> bool:
        response = requests.post(
            "https://apps.growmeorganic.com/api-product/trigger-company-explorer-task",
            headers=self.headers,
            data={"country": country, "industry": industry, "size": size},
        )

        if response.status_code == 200:
            return response.json()

    def get_report(self, country: str, industry: str, size: str) -> dict:
        response = requests.get(
            "https://apps.growmeorganic.com/api-product/load-companies-tasks-exported",
            headers=self.headers,
        ).json()["data"]

        filtered = list(
            filter(
                lambda x: x["country"] == country
                and x["industry"] == industry
                and x["size"] == size,
                response,
            )
        )

        return pd.read_csv(filtered[0]["file_csv"])  # change to sort_values

