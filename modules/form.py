def getForm(isSuccess, message, result):
    return {
        'isSuccess': isSuccess,
        'message': message,
        'result': result
    };

def getSuccessForm(message, result):
    return getForm(True, message, result)

def getFailureForm(message):
    return getForm(True, message, {})