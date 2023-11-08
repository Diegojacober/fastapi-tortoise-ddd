from adapter.post import PostTortoiseAdapter
from adapter.schemas.post import PostModel
from domain.service.post import PostService


def post_factory():
    adapter = PostTortoiseAdapter(model=PostModel)
    service = PostService(adapter=adapter)
    return service