from fastapi import APIRouter
from app.api.endpoints import user, api, monitor, email_group, settings

router = APIRouter()
router.include_router(user.router, prefix="/users", tags=["users"])
router.include_router(api.router, prefix="/apis", tags=["apis"])
router.include_router(monitor.router, prefix="/monitor", tags=["monitor"])
router.include_router(email_group.router, prefix="/email-groups", tags=["email-groups"])
router.include_router(settings.router, prefix="/settings", tags=["settings"])