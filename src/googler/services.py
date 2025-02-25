import uuid
from django.contrib.auth import get_user_model

User = get_user_model()

def generate_unique_username(
    id_info,
    use_uuid=False,
    uuid_length=4,
    max_attempts=3,
    attempt=0,
    check_existing=False,
):
    use_google_username = False
    if "@gmail.com" in id_info.get("email"):
        use_google_username = True

    if not use_google_username:
        given_name = id_info.get("given_name") or ""
        last_name = id_info.get("family_name") or ""
        uuid_str = None
        if use_uuid:
            uuid_str = str(uuid.uuid4()).replace("-", "")[:8]

        username = ".".join([given_name, last_name, uuid_str])
        username = username.rstrip(".")
        username = username.lower()
        username = username.strip()
    else:
        google_username = id_info.get("email")
        username = google_username.replace("@gmail.com", "")
    if check_existing:
        qs = User.objects.filter(username__startswith=username)
        if qs.exists():
            attempt += 1
            if attempt > max_attempts:
                return f"user-{uuid.uuid4()}"
            return generate_unique_username(
                id_info, use_uuid, uuid_length, max_attempts, attempt
            )
    return username


def get_or_create_google_user(google_user_info):
    email = google_user_info.get("email")
    if not email:
        raise ValueError("No email provided by Google")

    try:
        user = User.objects.get(email=email)
    except User.DoesNotExist:
        # Create new user
        username = generate_unique_username(google_user_info, use_uuid=True)
        user = User.objects.create_user(
            email=email,
            username=username,
            first_name=google_user_info.get("given_name", ""),
            last_name=google_user_info.get("family_name", ""),
        )
        user.set_unusable_password()
        # You might want to mark this user as having been created through Google OAuth
        user.save()

    return user