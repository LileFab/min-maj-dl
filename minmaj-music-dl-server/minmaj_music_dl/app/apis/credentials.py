from ninja import Router
from app.schemas import CredentialSchema, AddCredentialSchema
from app.services import credentials as credentials_sv

router = Router()


# /credentials
@router.get("/", response=CredentialSchema | None)
def get(request):
    return credentials_sv.get()


@router.post("/create-or-update", response=CredentialSchema | None)
def create_or_update(request, credentials: AddCredentialSchema):
    return credentials_sv.create_or_update(credentials=credentials)
