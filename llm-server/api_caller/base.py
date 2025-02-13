from typing import Dict

from langchain.chains.openai_functions.openapi import get_openapi_chain
from langchain.utilities.openapi import OpenAPISpec


def try_to_match_and_call_api_endpoint(
    swagger_spec: OpenAPISpec, text: str, headers: Dict[str, str]
) -> str:
    openapi_call_chain = get_openapi_chain(swagger_spec, verbose=True, headers=headers)

    return openapi_call_chain.run(text)
