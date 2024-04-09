import requests
from abc import ABC, abstractmethod
from typing import Dict, List, Union

class APIResearchInterface(ABC):


    @abstractmethod
    def get(self, *args, **kwargs) -> Union[Dict, List]:
        pass


class APIResearch(APIResearchInterface):


    def __init__(self, endpoint:str=None) -> None:
        self._endpoint = endpoint


    def get(self, *args, **kwargs) -> Union[Dict, List]:
        if not self.endpoint:raise TypeError("No endpoint was provided. Set endpoint property before making any request")
        try:
            response = requests.get(self.endpoint, *args, **kwargs)
            response.raise_for_status()
        except Exception as e:
            raise Exception(e)
        else:
            return response.json()


    @property
    def endpoint(self) -> str:
        return self._endpoint


    @endpoint.setter
    def endpoint(self, endpoint:str) -> None:
        if not isinstance(endpoint, str):
            raise TypeError(f"endpoint must be a URL of type str, \"{endpoint}\" of type {type(endpoint)} was provided.")
        self._endpoint = endpoint


class OpenLibraryAPIResearch:
    
    
    def __init__(self, api: APIResearch) -> None:
        if not isinstance(api, APIResearch): raise TypeError(f"api argument must be of type :class: APIResearch, {api} of type {type(api)} was provided.")
        self._api = api
    
    
    def get(self, query_type: str, value: str) -> None:
        return self.api.get(params={query_type: value})
    

    @property
    def api(self) -> APIResearch:
        return self._api


    @api.setter
    def api(self, api: APIResearch) -> None:
        if not isinstance(api, APIResearch):raise TypeError(f"api argument must be of type :class: APIResearch, {api} of type {type(api)} was provided.")
        self._api = api


if __name__ == "__main__":
    myapi = APIResearch("https://openlibrary.org/search.json")
    response = myapi.get()
    
    ol = OpenLibraryAPIResearch(myapi)
    print(ol.get("title", "lord of the rings"))
    