from rest_framework.mixins import CreateModelMixin
from rest_framework.viewsets import GenericViewSet

from pydis_site.apps.api.models.bot.message_deletion_context import MessageDeletionContext
from pydis_site.apps.api.serializers import MessageDeletionContextSerializer


class DeletedMessageViewSet(CreateModelMixin, GenericViewSet):
    """
    View providing support for posting bulk deletion logs generated by the bot.

    ## Routes
    ### POST /bot/deleted-messages
    Post messages from bulk deletion logs.

    #### Body schema
    >>> {
    ...     # The member ID of the original actor, if applicable.
    ...     # If a member ID is given, it must be present on the site.
    ...     'actor': Optional[int]
    ...     'creation': datetime,
    ...     'messages': [
    ...         {
    ...             'id': int,
    ...             'author': int,
    ...             'channel_id': int,
    ...             'content': str,
    ...             'embeds': [
    ...                 # Discord embed objects
    ...             ]
    ...         }
    ...     ]
    ... }

    #### Status codes
    - 204: returned on success
    """

    queryset = MessageDeletionContext.objects.all()
    serializer_class = MessageDeletionContextSerializer