from app.models import Credential
from app.schemas import CredentialSchema, AddCredentialSchema


def get() -> Credential | None:
    return Credential.objects.first()


def create_or_update(credentials: AddCredentialSchema) -> Credential | None:
    if credentials:
        old_creds = Credential.objects.first()
        if old_creds is None:
            cred_data = credentials.model_dump(exclude_none=True)
            cred = Credential.objects.create(**cred_data)
            return cred
        else:
            for field, value in cred_data.items():
                setattr(old_creds, field, value)
            old_creds.save()
            return old_creds
    else:
        return None
