from voluptuous import Schema, PREVENT_EXTRA

create_single_user = Schema(
    {
        "name": str,
        "job": str,
        "id": str,
        "createdAt": str
    },
    extra=PREVENT_EXTRA,
    required=True
)

update_single_user = Schema(
    {
        "name": str,
        "job": str,
        "updatedAt": str
    },
    extra=PREVENT_EXTRA,
    required=True
)

login_successfully = Schema(
    {
        "token": str
    },
    extra=PREVENT_EXTRA,
    required=True
)