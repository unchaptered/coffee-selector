def getForm(isSuccess, message, result):
    """
    일정한 형태의 객체를 반환하는 순수함수입니다.
    ```python
        isSuccess: boolean
        message: string
        result: Object
    ```
    """
    return {
        'isSuccess': isSuccess,
        'message': message,
        'result': result
    };

def getSuccessForm(message, result):
    """
    일정한 형태의 객체를 반환하는 순수함수입니다.
    ```python
        isSuccess: True
        message: string
        result: Object
    ```
    """
    return getForm(True, message, result)

def getFailureForm(message):
    """
    일정한 형태의 객체를 반환하는 순수함수입니다.
    ```python
        isSuccess: False
        message: string
        result: {}
    ```
    """
    return getForm(False, message, {})