
# **setting_api.py**
"""Hello World API implemented using Google Cloud Endpoints.

Contains declarations of endpoint, endpoint methods,
as well as the ProtoRPC message class and container required
for endpoint method definition.
"""
import endpoints
from protorpc import messages
from protorpc import message_types
from protorpc import remote


# If the request contains path or querystring arguments,
# you cannot use a simple Message class.
# Instead, you must use a ResourceContainer class
REQUEST_CONTAINER = endpoints.ResourceContainer(
    message_types.VoidMessage,
    name=messages.StringField(1),
)


package = 'Hello'


class Hello(messages.Message):
    """String that stores a message."""
    welcome = messages.StringField(1)


@endpoints.api(name='helloworldendpoints', version='v1')
class HelloWorldApi(remote.Service):
    """Helloworld API v1."""

APPLICATION = endpoints.api_server([HelloWorldApi])
