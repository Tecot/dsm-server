from app.models import TaskInfoModel

def get_task_statuses_service(keys_str):
    print(keys_str)
    keys = keys_str.split('$')
    keys_info = []
    for key in keys:
        key_info = TaskInfoModel.objects.get(key=key)
        keys_info.append({
            'key': key_info.key,
            'status': key_info.status
        })
    result = {
        'data': keys_info
    }
    return result