def validate_name(name: str) -> str or None:
    """
    이름은 3자 이상 10자 이하이어야 합니다.

    유효한 값이면 name 을 반환하고 아니라면 None 읇 반환합니다.

    `@returns` str or None
    """
    length = len(name)

    is_valid = 3 <= length <= 10

    if is_valid:
        return name
    else:
        return


def validate_password(pw: str) -> str or None:
    """
    비밀번호는 3자 이상 30자 이하이어야 합니다.

    유효한 값이면 pw 를 반환하고 아니라면 None 을 반환합니다.

    `@returns` str or None
    """
    length = len(pw)

    is_valid = 3 <= length <= 30

    if is_valid:
        return pw
    else:
        return
