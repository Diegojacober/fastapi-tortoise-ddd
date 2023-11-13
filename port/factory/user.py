from adapter.user import UserTortoiseAdapter
from adapter.models.user import UserModel
from domain.service.user import UserService


def user_factory():
    adapter = UserTortoiseAdapter(model=UserModel)
    service = UserService(adapter=adapter)
    return service