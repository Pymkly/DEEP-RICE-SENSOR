import logging

from fastapi import APIRouter, Request

from api.incoming.manager import IncomingManager
from api.utils.config import get_ref_from_mac, on_mac_unknown

router = APIRouter()

manager = IncomingManager()


@router.get("/")
async def receive_data(request: Request):
    params = dict(request.query_params)
    logging.info(params)
    mac = params.pop("mac", None)
    ref = get_ref_from_mac(mac)
    logging.info(ref)
    # print(ref)
    if ref is None:
        on_mac_unknown(mac)
    else:
        manager.parse_and_save(ref=ref, raw_data=params)
    return {"status": "ok", "saved": True}
