import collections
import typing as t

import hikari

__all__ = ["Duck"]

_ListenerT = t.Callable[[hikari.Event], t.Coroutine[t.Any, t.Any, None]]


class Duck:
    def __init__(
        self, prefix: t.Optional[str], intents: hikari.Intents = hikari.Intents.ALL_UNPRIVILEGED, **kwargs: t.Any
    ) -> None:
        self._prefix: t.Optional[str] = prefix
        self._intents: hikari.Intents = intents
        self._hikari_bot: t.Optional[hikari.GatewayBot] = None
        self._extra_kwargs: t.Dict[str, t.Any] = kwargs
        self._listeners: t.Dict[t.Type[hikari.Event], t.List[_ListenerT]] = collections.defaultdict(list)

    def listen(self, event: t.Type[hikari.Event]) -> t.Callable[[_ListenerT], _ListenerT]:
        def decorate(func: _ListenerT) -> _ListenerT:
            self._listeners[event].append(func)
            return func

        return decorate

    async def on_message_create(self, event: hikari.MessageCreateEvent) -> None:
        assert self._prefix is not None

        if event.message.author.is_bot:
            return

        # Do command processing here :beanos:

    def run(self, token: str, **kwargs: t.Any) -> None:
        self._hikari_bot = hikari.GatewayBot(token, intents=self._intents, **self._extra_kwargs)

        if self._prefix is not None:
            self._hikari_bot.subscribe(hikari.MessageCreateEvent, self.on_message_create)

        for event, listeners in self._listeners.items():
            for listener in listeners:
                self._hikari_bot.subscribe(event, listener)

        self._hikari_bot.run(**kwargs)
